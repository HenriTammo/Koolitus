Tsükli jätk oleks continue ja lõpetus oleks break

WHILE:

Sarnane IF funktsioonile, kastuad siis kui ei tea mitu korda on vaja 
läbi käia

while True: #versioon ilma muutujata, et lõpetada, kasuta break
while muutuja == True:#saab muuta muutuja False-iks või breakida
while muutuja == "tere":#muutuja võib võrduda stringiga, intiga, floatiga, booleaniga
#või teise muutujaga
while nr<10 and nr>0#nagu iffis, saab numbrite järgi määrata, lõpetamiseks break
#and asemel saab ka OR kasutada või ka mõlemat korraga

FOR:

Kaks eri kasutust, kas arvuline lugemine või väärtuse omistamine lugejale(x)

for x in range():#x võib nimetada kuidas iganes soovid
#sulgude sisse on vaja panna kas täisarv või loetav muutuja
#kasutades len() funktsionaalsust, saab lugeda ka sõnastike või nimekirju
#siin kehtib ka break
for y in ...: #seda saab kasutada selleks, kui on vaja väärtus
kuskilt hulgast kätte saada
#saab lugeda sisse ka stringe(nii muutuja kui ka niisama sõna), siis võtab 
täht tähe haaval
#sõnastike ja nimekirju saab lihtsalt sisestada siia, ilma len() funktsioonita

for x, y in sõnastik: #niimodi saad võtta sõnastikust nii nime kui ka väärtuse