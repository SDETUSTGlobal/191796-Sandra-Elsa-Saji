
#Code for while loop	
x=0    
while (x<4):
    print (x)
    x= x+1
print("__________________________________")	
#For Loop Simple Example	
x=0 
for x in range (2,7):
    print (x)
print("__________________________________")	
#Use of for loop in string	
Months = ["Jan","Feb","Mar","April","May","June"]
for m in (Months):
    print (m)
print("__________________________________")	
#Use break-statement in for loop	
for x in range (10,20):
       if (x == 15): break
       print (x)
print("__________________________________")	   
#Use of Continue statement in for loop	
for x in range (10,20):
       if (x % 5 == 0): continue
       print (x)
print("__________________________________")	   
#Code for “enumerate function” with “for loop”	
Months = ["Jan","Feb","Mar","April","May","June"]
for i, m in enumerate (Months):
    print (i,m)