# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	multiplication=num1*num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2):
    	if num2 is 0:
    			return 0
    	else:
    			division=num1/num2
    			return division					
    		

def power(num1, num2): #num1 ^ num2
    if num2 is 0 and num1 is 0:
    		return 0
    power=1.0
    for i in range(num2):
    		power*=num1
    return power
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n):
    temp=a
    gp=[]
    for i in range(n):
            gp.append(temp)
            temp*=r
    return gp
    		

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
    temp=a
    ap=[]
    for i in range(n):
        ap.append(temp)
        temp+=d
    return ap

# # Python 3 program to print HP.   Harmonic Progression
# #You cant use the inbuilt python function. Write your own function
# def printHP(a, d, n): 
# 	hp=[]
# 	return hp