While Loops
-for Loops
condition is true,while loop execute a set of statements

x = 1
while x < 7:
	print(x)
	x += 1


While loop require variable ready
 x = 50
 while x < 100:
 	print(x)
 	if x == 5:
 		break
 	x += 5 


 For Loops
 #for loops is iterating over a sequence

 fruits = ["apple","banana","orange","pineapple","coconut","cucumber"]
 for x in fruits:
 		print(x)

 #looping in a string

 for x in "pineapple":
 	print(x)

 #The break Statement

 #stop after condition

 fruits = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruits:
 		print(x)
 		if x == "pineapple":
 			break




---
#stop before condition

fruits = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruits:
 		if x == "pineapple":
 			break
 		print(x)
 			
#stop condition Statement - Stop the current iteration

fruits = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruits:
 		if x == "pineapple":
 			continue
 		print(x)

for x in range(10):
	print(x)

for x in range(10, 100):
	print(x)

for x in range(10, 100, 5):
	print(x)


#Nested Loops
NumberA = {1, 2, 3, 4, 5}
NumberB = {1, 2, 3, 4, 5}

for x in NumberA:
	for y in NumberB:
		print(x,y,z)

NumberA = {1, 2, 3, 4, 5}
>>> NumberB = {1, 2, 3, 4, 5}
>>> NumberC = {1, 2, 3, 4, 5}
>>> for x in NumberA:
...     for y in NumberB:
...             for z in NumberC:
...                     print(x,y,z)
...

#Pass
for x in [1, 2, 3, 4, 5]:
	if x == 3:
		pass
	print(x)

-----------

words = ['cat','window','defenestrate']
for w in words:
	print(w, len(w))


----------

for n in range(2, 20):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break

	else:
		#loop fell theough without finding a factor
		print(n, 'is a prime number')

--------



>>> for n in range(2, 10):
...     for x in range(2, n):
...             if n % x == 0:
...                     print(n, 'equals', x, '*', n//x)
...                     break
...     else:
...             print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
>>> for n in range(2, 21):
...     for x in range(2, n):
...             if n % x == 0:
...                     print(n, 'equals', x, '*', n//x)
...                     break
...     else:
...             print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
10 equals 2 * 5
11 is a prime number
12 equals 2 * 6

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
		num +=10
		print("Number is", num)
	print("Found a  number", num)

