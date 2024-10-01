#List Comprehension
#print numbers from 1 to 100
print("Printing numbers from 1 to 100:")
n=[num for num in range(1,101)]
print(n)

#printing even numbers from 1 to 100
print("Printing even numbers from 1 to 100:")
n=[num for num in range(1,101) if num%2==0]
print(n)

#printing numbers from 1 to 100 that are divisible by 7
print("Printing numbers from 1 to 100 that are divisible by 7:")
n=[num for num in range(1,101) if num%7==0]
print(n)

#printing squares of even numbers from 1 to 20 
print("Printing squares of even numbers from 1 to 20:")
n=[num**2 for num in range(1,21) if num%2==0]
print(n)

#printing numbers form 50 to 1
print("Printing numbers form 50 to 1:")
num=[x for x in range(50,0,-1)]
print(num)

#printing all the vowels from the given sentence
sentence="The rocket came back from mars"
print(sentence)
print("Printing all the vowels from the given sentence:")
v=[char for char in sentence if char in"AEIOUaeiou"]
print(v)

#program to convert the negative prices to 0 from the given list
list=[1,2,-3,5.6,7,-9]
print("Original prices:",list)
p=[x if x>0 else 0 for x in list]
print(p)