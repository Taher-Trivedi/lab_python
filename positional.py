# basic positional argument
def add (a,b):
    print("a=",a)
    print("b=",b)
    print(a+b)
result = add (2,5)
print("sum=",result)

# student information

def student_info (name,roll,marks):
    print("name:",name)
    print("roll no:",roll)
    print("marks:",marks)  
student_info("ravi",101,85)

# simple intrest

def simple_intrest (p,r,n):
    si=(p*r*n)/100
    print("simple intrest:",si)
simple_intrest (10000,2,2)
simple_intrest (50000,1.2,3)

# area of circle
def area_circle(r):
    area = (3.14 * r * r)
    print("Area of circle (r=" + str(r) + "):", area)
area_circle(1.5)
area_circle(4)

# check number positive nagative or zero
def check_number(n):
    if n > 0:
        print(f"{n} is Positive")
    elif n < 0:
        print(f"{n} is Negative")
    else:
        print(f"{n} is Zero")
        
        
        def check_even_odd(n):
              if n % 2 == 0:
                  return f"{n} is Even"
              else:
                   return f"{n} is Odd"

                  
        
   
       