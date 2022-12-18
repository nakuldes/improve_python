list1 = ['    <sadsd@gnmg.com', '   \t<rgrg>  ']
cc =''
cc1=''
for i in list1:
    i = i.strip()
    pos=i.index('<')
    cc = i[pos:len(i)-1]
    cc1 = cc1 + cc + ',\n'

print(cc1)