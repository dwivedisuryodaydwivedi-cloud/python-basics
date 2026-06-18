number_list = [10,20,30,40,50]
print(type(number_list))
print(len(number_list))
print(id(number_list))
print(number_list[0])
print(number_list[1])
print(number_list[2])
print(number_list[3])
print(number_list[4])
add_list = number_list[0] + number_list[1] + number_list[2] + number_list[3] + number_list[4]  
average = add_list/len(number_list)
print(average)