#1 square number 
def sqr(num, exp=2):
    return num ** exp

print(sqr(3))     
print(sqr(3, 3))   
print(sqr(2, 4))   

#2 default name
def greet(name="Guest"):
    print("Hello", name)

greet()      
greet("Alice") 

#3 sum of value
def add(a, b=5):
    print("Sum:", a + b)

add(10, 5)   
add(10)      

#4 
def add_numbers(arr=[10, 20]):
    total = 0
    for num in arr:
        total += num
    return total

print("Add numbers:", add_numbers([10, 20]))
print("Add numbers:", add_numbers([5, 10, 15, 20]))
print("Add numbers:", add_numbers()) 