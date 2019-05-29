ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
num=int(input("Enter one number: "))
answer=""
if num>=1000 and num<=9999:
	answer+=ones[int(num/1000)]+ " thousand "
	num=num%1000
if num>=100:
	answer+=ones[int(num/100)]+ " hundred "
	num=num%100
if num>=20:
	answer+=tens[int(num/10)]
	num=num%10
if num>0 and num<=19:
	answer+=ones[num]
print(answer)