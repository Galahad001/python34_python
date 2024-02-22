from decimal import Decimal
import datetime
DATE_D = '%Y-%m-%d'
goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('5'), 'expiration_date': datetime.date(2024, 2, 20)},
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2024, 6, 19)}
    ],
    'Вода': [{'amount': Decimal('1.5'), 'expiration_date': None}],
    'Яйца': [{'amount': Decimal('2'), 'expiration_date': None}],
    'Морковь': [ 
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 8, 6)}
    ],
    'Старые пельмени':[
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2024, 6, 17)}
    ]
} 

def add(items, title, amount, expiration_date=None):
    key = items.keys()
    if expiration_date != None:
        f_date_str = datetime.datetime.strptime(expiration_date, DATE_D)
        f_date = f_date_str.date()
        if title in key:
           items[title].append({'amount':amount, 'expiration_date':f_date})
        else:
           items[title] = [{'amount':amount, 'expiration_date':f_date}]
    else:
        if title in key:
           items[title].append({'amount':amount, 'expiration_date':expiration_date})
        else:
           items[title] = [{'amount':amount, 'expiration_date':expiration_date}]
        
#add(goods, 'Яйца Фабрики №1', Decimal('4'), '2023-07-15')
#print(goods)

def add_by_note(items, note):
    key = items.keys()
    spis = note.split(' ')
    date_test = spis[-1]
    if date_test.find('-') != -1:
        f_num = float(spis[-2])
        amount = Decimal(f_num)
        date_test = datetime.datetime.strptime(spis[-1], '%Y-%m-%d').date() 
        title = spis[0:len(spis)-2]
        title_res = ' '.join(title)
        if title_res in key:
               items[title_res].append({'amount':amount, 'expiration_date':date_test})
        else:
               items[title_res] = [{'amount': amount, 'expiration_date':date_test}]
    else:
        f_num = float(spis[-1])
        amount = Decimal(f_num)
        title = spis[0:len(spis)-1]
        title_res = ' '.join(title)
        if title_res in key:
               items[title_res].append({'amount':amount, 'expiration_date':None})
        else:
               items[title_res] = [{'amount': amount, 'expiration_date':None}]
        
    
#add_by_note(goods, 'Яйца Фабрики №1 4.5 2023-07-15')       
#print(goods)

def find(items, needle):
    spis = []
    for i in items.keys():
        if needle.lower() in i.lower():
            spis.append(i)
    return spis

#print(find(goods, 'А'))


def amount(items, needle):
    count = 0
    key_s = list(items.keys())
    if needle in key_s:
        for i in items[needle]:
            count += i['amount']
        return count
    
    for key_ch ,value in items.items():
        k = key_ch.lower()
        n = needle.lower()
        if k.find(n) != -1:
            for i in items[key_ch]:
               count += i['amount']
     
    if count != 0:     
        return count 
            
    if needle not in key_s:
        return Decimal('0')
    
#print(amount(goods, 'пель'))




def expire(items, in_advance_days=0):
    result_expire = []
    date_now = datetime.date.today()
    amount_day = datetime.timedelta(days = in_advance_days)
    print('NOW',date_now)
    print('AMOUNT DAY',amount_day)
    for i in items:
        for j in items[i]:
            if j['expiration_date'] != None:
                print('DELTA', j['expiration_date'] - date_now)
                if (j['expiration_date'] - date_now) <= amount_day:
                    amount(items,i)
                    list.append(result_expire, (i, amount(items,i)))

    return result_expire 
print(expire(goods, 2))