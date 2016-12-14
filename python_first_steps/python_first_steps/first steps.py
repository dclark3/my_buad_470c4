# This is a simple demonstration to show how to use python in a text editor
import sys 

for i in range (50):
    print("hello world")

val = 0
for i in range(10,20):
	val += i
print("sum: " + str(val))

coords = []
totals=(0,0)
for i in range (1,11):
	for j in range(20,31):
		coords.append((i,j))
		a, b = totals
		totals = (a+i, b+j)
print("Coords: " + str(coords))


val = 0
minI = 0
maxI = 20
print("COMMAND LINE INPUT: "  + str(sys.argv)) #how to pass inputs in args
if len(sys.argv) > 1: 
	minI = sys.argv[1]
	minI = int(minI)
		
if len(sys.argv) > 2:
	
	maxI = sys.argv[2]
	maxI = int(maxI)

print("print test min: " +str(minI))	
print("print test max: " +str(maxI))

counter = minI
while counter <= maxI:
	val += counter
	counter += 1
	
print("While Sum: " + str(val))


#counter = minI
#while counter <= maxI:
#val += counter
	#counter += 1
#print("While sum: " + str(val))


	