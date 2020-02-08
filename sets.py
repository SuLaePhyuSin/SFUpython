#Sets

Sets.py

inculdes a date type for sets.
Curly braces or the set() function can be used to create sets.

basket = {'apple', 'orange', 'applpe', 'pear', 'orange', 'banana'}
print(basket)		#show that duplicates have been removed

'orange' in basket				#first membership testiong 
'crabages' in basket


Demonstrate set operation on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a     						#unique letters in a
a = b   					#letters in a but not in b
a | b 						#letters in a or b or both
a & b  						#letters in both a and b
a * b 						#letters in a or b but noth both


x = set ('23802348')
y = set('57839012')
a = {x for x in  'abracadabra' if x not in 'abc'}


--------

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.update("grape")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits


>>> Distionaries

#Disionaries
#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape' : 4139}
tel['sape']
tel['guido'] = 4127
tel


del tel ['sape']
tel['irv'] = 4137
tel

list(tel) # change to list

sorted(student) #Alphabet Sorting

"MgOo" in student

"Mama" not in student 

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(scope=4134, guido=4127, jack=4098) 


{x: x**2 for x in(2, 4, 6)}

for x in 2, 4 , 6:
	print(x: x**2)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
 for k, v in knights.items():
 	print(k, v)
 	knights = {'gallahad': 'the pure', 'robin': 'the brave', 'sape': 4335}
>>> for i,v in enumerate(['tics', 'tac', 'toe']):
...     print(i,v)s