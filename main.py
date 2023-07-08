a=12
print(a)
b=65
print(b)
#we can add a and b (it should be of same type)
print(a+b)

# for variable, we have to keep it in double quotes
c="syed"
print(c)
# we cannot add a and c
# we can add c and d
d="mohsin"
print(d)
print(c+d)


# for knowing the type
print("the type of a is", type(a))
print("the type of b is",type(b))
print("the type of c is",type(c))
print("the type of d is",type(d))



list=(4, 3, -5, 5.5, [-5+2])   #both brackets can be used
print(list)
list1=["syed","mohsin","aijaz"]
print(list1)
#list can be used for both(integers and  variables)
list2= [2,3,2.4, -4, [-3+2], ["syed", "mohsin", "aijaz"]]
print(list2)


touple=("syed","mohsin", "aijaz")   #trouple cannot be used for integers
print(touple)


#for marks election etc
dict={"name":"syed mohsin", "age":22, "canVote":True}
print(dict)
dict1={"name":"syed", "age":17, "canVote":False}
print(dict1)

dict2={"name":"syed mohsin aijaz","roll":2231591,"marks":300,"pass":True}
print(dict2)
#use True or False