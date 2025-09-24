# def number_split(n):
#     left = n// 2
#     right =n-left
#     return[left,right]

# print (number_split(4)) 
# print (number_split(10))
# print (number_split(11)) 
# print (number_split(-9))

# def list_sort(lst,s):
#     m = asc_des_none
#     if s == "Asc":
#         return sorted(lst)
#     elif s == "des":
#         return sorted(lst,reverse=True)
#     elif s == "none":
#         return lst
# print([4, 3, 2, 1],"Asc")
# print([7, 8, 11, 66], "Des")
# print( "None")


# def find_even_nums(n):
#     return[i for i in range(2,n+1)if i % 2== 0]

# print(find_even_nums(8))
# print(find_even_nums(4))
# print(find_even_nums(2))


# def my_function():
#     var = 2
#     print("do I know that variable",var)

# var = 1
# my_function()
# print(var)


# a = 1
# def fun():
#     global a
#     a=2
#     print(a)

# fun()
# a = 3
# print(a)


# a = 1
# def fun():
#     global a
#     a = 2
#     print(a)

# a=3
# fun()
# print(a)


# def unique_sort(lst):
#     return list(set(lst))

# print(unique_sort([1, 2, 4, 3])) 
# print (unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2])) 
# print (unique_sort([6, 7, 3, 2, 1]))
