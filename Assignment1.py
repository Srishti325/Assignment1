
# coding: utf-8

# # wap find the area and perimter of the square
# 

# In[4]:


print("Enter 'x' for exit.");
side = input("Enter side length of square: ");
if side == 'x':
    exit();
else:
    slength = int(side);
    perimeter = 4*slength;
    print("\nPerimeter of Square =", perimeter);


# # wap find the area and perimter of the rectangle
# 

# In[5]:


print("Enter 'x' for exit.");
leng = input("Enter length of rectangle: ");
if leng == 'x':
    exit();
else:
    brea = input("Enter breadth of rectangle: ");
    length = int(leng);
    breadth = int(brea);
    perimeter = (2*length) + (2*breadth);
    print("\nPerimeter of Rectangle =", perimeter);


# # wap find the area and perimter of the triangle

# In[2]:


# Three sides of the triangle a, b and c are provided by the user
 
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
 
# calculate the semi-perimeter
s = (a + b + c) / 2
 
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# # wap find the simple intrest

# In[7]:


P = 10 
R = 12 
T = 3 
  
# Calculates simple interest  
SI = (P * R * T) / 100
  
# Print the resultant value of SI  
print("simple interest is", SI) 


# # wap find sum of the 1st N natural number
# 

# In[8]:


n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)


# # wap find the sum of the squares of the 1st Natural

# In[9]:


def squaresum(n) : 
  
    # Iterate i from 1  
    # and n finding  
    # square of i and 
    # add to sum. 
    sm = 0
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
      
    return sm 
  
# Driven Program 
n = 4
print(squaresum(n))


# # wap find the sum of the cubes of the 1st Natural

# In[10]:


def sumOfSeries(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i 
          
    return sum
  
   
# Driver Function 
n = 5
print(sumOfSeries(n)) 

