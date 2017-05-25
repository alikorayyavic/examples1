l1 = [1,2,39,5,3]
sum = 0
for i in l1:
	sum=sum + i
	print(i)
print(sum)

for x in range(5):
	print (x)

l2 = range(15,2,-2)
print (l2)

for x in range(1,20):
	if(x%3==0):
		continue
	print (x)
	
for x in range(1,20):
	if(x%3==0):
		break
	print(x)	
print("the series is over")	


result=[]
for i in range(1,100):
	for b in range(2,i):
		if(i%b==0):
			break
	else:
		result.append(i)
print(result)
			