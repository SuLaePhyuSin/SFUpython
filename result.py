import studentx
import maryo

x = studentx.a["code"]
y = studentx.b["code"]
z = studentx.a["student"]

print(x, ' ',y,' ',z)

v = studentx.a["mother"]
print(v)

t = studentx.b["student"]
print(t)

h = studentx.b["father"]
print(h)

for i in range(len(maryo.a)):
	print(i, maryo.a[i])
