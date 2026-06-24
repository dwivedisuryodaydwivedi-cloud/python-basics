# printing the given list of element in asecending and descending order
data = [11,8,10,5,19,18,21,32,45]
print("Original list of order is ", data)

for i in range(0,len(data)-1): # To make list in ascending oder 
    
    for j in range(len(data)-1):
        
        if data[j] > data[j+1]:
            
            temp = data[j]
            
            data[j] = data[j+1]
            
            data[j+1] = temp
            
print("Ascending order of list is ",data)

# TO make list in descending order 

for i in range(0,(len(data)-1)//2):
    
    temp = data[i]
    
    data[i] = data[len(data)-1-i]
    
    data[len(data)-1-i] = temp
    
print("desecnding order of an list of data ",data);;

# Inserting the given element at specific position of list 

