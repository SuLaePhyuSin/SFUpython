#Boolean Experssion

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))



Python Conditions










x = 70
>>> y = 60
>>> if x > y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is greater than y


x is greater than y
>>> if x > y :
...     print("x is greater than y")
... elif x >= y:
...     print("x is greater or equal to y")
... elif y <x:
...     print("y is smaller than x")
... else:
...     print("x is nothing")
...
x is greater than y

x = 70
>>> y = 60
>>> if x > y
  File "<stdin>", line 1
    if x > y
           ^
#short Hand if
>>> if x > y: print ("x is greater than y")
...
x is greater than y
>>>

x = 50
y = 150
print(x) if x > y else print(y)

 x = 50
>>> y = 40
>>> z = 100
>>> if x < y and z > x:
...     print("All Conditions are True")
... else:
...     print("Some Conditionos are False")
...
Some Conditionos are False
>>>


 if x > y and z > y and z > x:
...     print("Answer1")
... elif x ==y or z == y or z > y and x > y:
...     print("Answer2")
... elif z > y znd y < x or z > y:
		print("Answer 3")
	else:
		print("Default1")
 x = 50
>>> y = 40
>>> z = 100
>>> if x > y or z < y:
...     print("one of the conditions is True")
... elif x > y and z > y:
...     print("All conditions are True")
... else:
...     print("nothing else")
...
one of the conditions is True
>>>

if x > y and z > y and x > z:
	print("Answer1")
elif x == y or z == y or z > y and x > y:
    print("Answer2")
elif z > y znd y < x or z > y:
	print("Answer 3")
else:
	print("Default")

x = int(input("Number :"))
A <= 100 or 90
B <= 90 or 80
C <= 80 or 60
D <= 60 or 50
F < 50

x = 50

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No,x is not greater than 20")


If x > 10 and x != 10 or x > 20:
	print("x is greater than 10 and 20")
else:
	print("x is greater than 10 & 20")






if student
	if batch
		if gender
else 
	not 

student = "SFU"
	batch = "3"
		gender = "male" 
