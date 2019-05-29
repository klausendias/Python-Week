F=0
msg=input("Enter any message:")
what=input("What word are you looking for: ")
i=0
while i<len(msg):
	if msg[i]==what[0]:
		if msg[i:i+len(what)]==what:
			F=F+1
			i=i+ len(what)-1
	i=i+1
print(F)