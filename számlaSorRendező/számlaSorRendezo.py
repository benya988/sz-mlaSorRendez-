
from encodings import utf_8
from http.client import CONTINUE
import os
from xml.etree.ElementTree import tostring
eredetiSor = []
szamok = 0
szo= ""


f = open("orderDetail.htm")

sor = (f.read().split("<tr "))

for x in sor:
    if True:
        eredetiSor.append("<tr "+ x)
        print (str(szamok)+". "+ eredetiSor[szamok])
        szamok +=1
        continue 
    break
        
print("Varialhato sorok szama: "+ str(len(sor)))
print ("----------------------------------------\nOpciok: \nSor athelyezese: (ertelemszeruen), vagy \nlezaras: \"vege\" szoval\n----------------------------------------")
print ("1-3 sor: Head szekcio\n"+len(eredetiSor)-14+"-"+len(eredetiSor)+": Vevo adatai, egyeb beallitasok")
while szo != "vege":
    szo = input ("Valaszd ki az athelyezendo sor sorszamat:")
    if szo != "vege":
        szo2= input ("Valaszd ki, melyik sorba legyen athelyezve: ")
        ujSzo= eredetiSor[int(szo)]
        eredetiSor.insert(int(szo2), ujSzo)
        eredetiSor.remove(eredetiSor[int(szo)])   
        print("Sor athelyezve")
        continue
    
    break

for x in eredetiSor:
        szo += x+"\n"
        continue


with open ('output.htm', 'w') as file:

    file.write(szo)


 
print('Fajl kiirva: output.htm neven')

os.startfile('output.htm')










