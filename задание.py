f = open('books.csv')
doc = open('тест.txt', 'w')
schet = 0
avtor = input()
kolzap = 0
nazvan = 0
knigi = ''
i = 0
for s in f:
    s = f.readline()
    kolzap += 1
    tz1 = s.find(';')
    tz2 = s.find(';', tz1 + 1)
    tz3 = s.find(';', tz2 + 1)
    tz4 = s.find(';', tz3 + 1)
    tz5 = s.find(';', tz4 + 1)
    tz6 = s.find(';', tz5 + 1)
    name = s[tz1 + 1:tz2]
    if len(name) > 30:
        nazvan += 1
    if s.find(avtor) > 0 and s[tz6 + 7:tz6 + 11]=='2015' or s[tz6 + 7:tz6 + 11]=='2018':
        knigi = knigi + name + '\n'
    if i < 20:
        doc.write(s[tz3 + 1:tz4] + '. ' + s[tz1 + 1:tz2] + ' - ' + s[tz6 + 7:tz6 + 11] + '\n')
        i += 1
doc.close()
print(kolzap)
print(nazvan)
print(knigi)
