import datetime


DOB = datetime.date(1995, 7, 9)
print(DOB, end='\n')
present = datetime.date.today()
diff = present - DOB

print(DOB.strftime("%A, %B %d, %Y"))

print(diff)

exdate = '01/11/1996'
parsed_exdate = datetime.datetime.strptime(exdate, '%d/%m/%Y')
print(parsed_exdate.day)
#help(datetime.timedelta())