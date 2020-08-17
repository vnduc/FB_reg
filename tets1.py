from random import sample 

list1 = ["1", "2", "3", "4", "5", "6" , "7" , "8" , "9" , "0" ]  
tele = []
list_int = sample(list1,8)
list_int_new = "".join(list_int)
print(list_int_new)
