size= int(input("Enter the size = "))
lst = []
result = 0
for i in range (size):
    element =int(input("Enter the element you want in the list = "))
    lst.append(element)
print(lst)
for i in lst:
    print(result,"+",i,"=",result+i)   
    result= result + i
print("your final output will be : ",result)