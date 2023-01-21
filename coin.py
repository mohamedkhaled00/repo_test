print("1-bitcoin 2-ethereum  3-dogecoin  \n")
c=float(input("chose yor coin :"))
a=float(input("enter your amount "))
if c == 1:
    print(a," bitcoin","=",a*22,937.20,"$")
elif c == 2:
    print(a," ethereum ","=",a*1,651.54,"$")
elif c == 3:
    print(a," dogecoin ","=",a*0.087,"$")
else:
    print("error! ")