int=[1,2,3,4,5,6,7,8,9,10]
print(int)
roll=7
 
if roll not in int:
  int.append(roll)
else:
 print ("already found")
print(int)