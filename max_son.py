# numbers = [1,2,3,4,5,6,7]
# print(max(numbers))
# print(min(numbers))


# def juft_sonlar(numbers):
#     new_list = []
#     for number in numbers:
#         new_list.append(number ** 2)

#     return new_list
# print(juft_sonlar([1,2,3,4,5,6,7,8,9,10]))


# def toq_sonlar(numbers):
#     new_list = []
#     for number in numbers:
#         new_list.append(number ** 2)
#     return new_list

# # print(toq_sonlar(())
# print(toq_sonlar([1,2,3,4,5,6,7,8,9,10]))


def manfiy_musbat(m):
    manfiy =[]
    musbat =[]
    if m > 0:
        manfiy.append(m)
    elif m < 0:
        musbat.append(m)
    return manfiy,musbat

m= int(input("raqam kiriting"))
print(manfiy_musbat(m))




