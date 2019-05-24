Product = input ("Enter product name: ")
Price = input ("Enter product price: ")
Qty = input ("Enter product quantity: ")
Amount = float (Price)*int (Qty)
VAT = Amount*15/100
Bill = Amount+VAT
print("Your total bill for", Product, "is as follows")
print("Total Amount Without VAT:", Amount)
print("VAT:", VAT)
print("Your total bill including VAT is £", Bill)