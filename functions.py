def f(x):
	return x+10	
	
print(f(8))

def hi(parameter):
	if(type(parameter)==int):
		print("hi"+str(parameter))
	else:	
		print("hi"+parameter)

hi("koray")
hi("ali")
hi(10)


def fib(n):
    a,b = 0,1
    while a<n:
		print(a)
		a,b=b,a+b


fib(20)


def fact(n):
	a = 1
	result = 1
	while (a <= n):
		result = result * a
		a = a + 1
	return result
		
print(fact(5))	

#n!=n*(n-1)	

def facto(n):
	if(n==0):
		return 1
	return n*facto(n-1)	

print(facto(5)) 



#g(x,y)

def g(x,y=3):
	return  x + 5*y

print(g(2,5))
print(g(2))	  































    
