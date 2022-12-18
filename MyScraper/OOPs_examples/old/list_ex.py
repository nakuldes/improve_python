em = '"nakul, des" <na@wp.com>, "Al, K" <al.k@wp.com>, \n "Nahar, Pragati" <napa@wp.com>'

em1 = '"nakul, des" na@wp.com>'

cc=''
ls = em.split('>')
for i in ls[:-1]:
    pos = 0
    i = i.strip()
    if i.__contains__('<'):
        pos = i.index('<')
    ccVal = i[pos+1:len(i)]
    cc += ccVal + ',\n'

print(cc)