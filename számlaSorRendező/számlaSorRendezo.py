
from xml.etree.ElementTree import tostring

eredetiSor = []
ujSor = []
szamok = 0

f = open("orderDetail.htm")

sor = (f.read().split("<tr "))
print(len(sor))

for x in sor:
    if "FFFFFF" or "EEEEEE" in x:
        szamok = szamok+1
        continue
    else:
        continue
    print(szamok)
    break



