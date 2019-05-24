Bill = int(input ("Enter total bill:"))
MoneyPaid = int(input ("Enter money paid: "))
change = MoneyPaid-Bill
print ("The customer is owed £",change)
print("Please see the breakdown below")
if change//20>=1:
    print (change//20, "x £20 Notes")
    change=change%20
if change//10>=1:
	print (change//10, "x £10 Notes")
	change=change%10
if change//5>=1:
    print (change//5, "x £5 Notes")
    change=change%5
if change//2>=1:
    print (change//2, "x £2 Coins")
    change=change%2
if change//1>=1:
    print (change//1,"x £1 Coins")
    change=change%1