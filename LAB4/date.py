from datetime import datetime, timedelta

#1
current = datetime.now()
result = current - timedelta(days=5)

#print(result.strftime("%d-%m-%Y"))

#2
yesterday = datetime.now() - timedelta(days=1)
today = datetime.now()
tomorrow = datetime.now() + timedelta(days=1)
#print(yesterday.strftime('%d-%m-%Y'), today.strftime('%d-%m-%Y'), tomorrow.strftime('%d-%m-%Y'),sep='\n')

#3
cur = datetime.now()
cur = cur.replace(microsecond=0)
#print(cur)

#4
def difference(date1, date2):
    diff = date2 - date1
    return diff.total_seconds()
#print(difference(datetime.now(),datetime.now() + timedelta(days=1)))
