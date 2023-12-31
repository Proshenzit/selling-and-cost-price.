cp = float(input("ENTER YOUR COST PRICE: "))
sp = float(input("ENTER YOUR   SELLING PRICE: "))
if cp>sp:
    amount = cp-sp
    print("Loss",amount)
else:
    amount= sp-cp
    print("Profit",amount)
