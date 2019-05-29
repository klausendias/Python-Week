def tax(salary):
	if salary>1500:
		T=salary*20/100
	else:
		T=salary*15/100
	return T
salary=int(input("Enter your salary: "))
print ("Total tax =", tax(salary))
print ("Your net salary is", salary-tax(salary))