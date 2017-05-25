def func(a):
	print(a)
	
func(10)

def mayk(a,b):
	return a+b
	
print(mayk(2,3))



def koray(*b):
	print (b)
	for i in b:
		print(i)
		
koray(1,2,3,4,5)
koray(1)
koray(1,2,3)		


def sum(*a):
	sonuc=0
	for i in a:
		sonuc = sonuc + i
	return sonuc	
	
print (sum(2,3))	
print (sum(2,3,4,5))
print(sum(2))

def function(**a):
	for i in a :
		print(str(i) + str(a[i]))
		
function(a=2,b=3,c=4)