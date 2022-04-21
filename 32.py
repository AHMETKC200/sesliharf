


sayı=int(input("sayı giriniz "))
prime= True
for i in range(2,sayı):
    if sayı %i ==0:
        prime= False

if prime==True:
    print("sayı asaldır")
if prime==False:
    print("asal değildir")