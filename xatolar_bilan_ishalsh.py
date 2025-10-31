# def check_list(numbers):
#     if numbers == []:
#         return "list bosh"
#     else:
#         return "listni ichida mallumot bor", numbers
    
# numbers = [1,2,3,4,5,6]
# print(check_list(numbers))


# def check_students(students):
#     names = input("ismingiz kiriting:")
#     for name in students.keys():
#         if name == names:
#             return "bu oquvchi guruhda mavjud"
#         else:
#             return "bu oquvchiguruhda mavjud emas"
        
# print(check_students({"ziyoda":"yoldoshboyeva","bobur:" : "abduxamidov"}))



# try:
#     son = int(input("Son kiriting: "))
#     print(10 / son)
# except ZeroDivisionError:
#     print("0 ga bolinmaydi")
# except:
#     print("Noto'g'ri element")

# student = {"Bobur": "Abduxamidov"}

# try:
#     word=(input("soz kiriting"))
#     print(word in student)
# except:
#     print("bundey text mavjud emas")

# numbers = [2,4,6]
# try:
#     print(2 + 4 + 6 )

# except:
#     print("royxat bosh")

# finally:
#     print("ishlash tugadi")


# def avarge_value(numbers):
#     return sum(numbers) / len(numbers)


# print(avarge_value([2,4]))



try:
    word = input("So'z kiriitng")
    print(word, "->", len(word))

except:
    print("matn bosh")


