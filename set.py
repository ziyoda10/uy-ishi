

class Student:
    def init(self, name, age, course, score):
        self.name = name
        self.age = age
        self.course = course
        self.score = score

    def str(self):
        return f"Ismi: {self.name}, yoshi: {self.age}, kursi: {self.course}, ball: {self.score}"


# O'quvchilar ro'yxati
students = []

# Uchta o'quvchi ma'lumotini kiritish
for i in range(3):
    print(f"{i + 1}-o‘quvchi ma’lumotlarini kiriting:")
    name = input("Ismi: ")
    age = int(input("Yoshi: "))
    course = input("Kursi: ")
    score = float(input("Ball: "))

    student = Student(name, age, course, score)
    students.append(student)
    print()

# Har bir o‘quvchini chiqarish
for student in students:
    print(student)

# O‘rtacha ballni hisoblash
average = sum([s.score for s in students]) / len(students)
print(f"Umumiy ball: {average:.2f}")





# 1. Car klassi — mashina haqida ma'lumot saqlaydi
class Car:
    def init(self, model, year, price_per_hour):
        self.model = model
        self.year = year
        self.price_per_hour = price_per_hour


# 2. Customer klassi — mijoz haqida ma'lumot saqlaydi
class Customer:
    def init(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id


# 3. RentalService klassi — ijarani boshqaradi
class RentalService:
    def init(self):
        self.rented_cars = {}  # {customer_id: car}

    def rent_car(self, customer, car, hours):
        if customer.customer_id in self.rented_cars:
            print(f"{customer.name} allaqachon mashina ijaraga olgan.")
        else:
            self.rented_cars[customer.customer_id] = car
            total = car.price_per_hour * hours
            print(f"\nMijoz: {customer.name} (ID: {customer.customer_id})")
            print(f"Ijaraga olingan mashina: {car.model} ({car.year})")
            print(f"Ijaraning umumiy summasi: {total} so‘m")

    def return_car(self, customer, car):
        if customer.customer_id in self.rented_cars:
            del self.rented_cars[customer.customer_id]
            print(f"\n{customer.name} mashinani qaytardi: {car.model}")
        else:
            print(f"\n{customer.name} hech qanday mashina ijaraga olmagan.")

    def show_rented_cars(self):
        if not self.rented_cars:
            print("\nHozircha hech qanday mashina ijaraga olinmagan.")
        else:
            print("\nIjaradagi mashinalar:")
            for cid, car in self.rented_cars.items():
                print(f"ID: {cid} — {car.model} ({car.year})")


# --- Asosiy dastur qismi ---
service = RentalService()

# Foydalanuvchidan ma'lumot olish
name = input("Mijoz ismi: ")
customer_id = input("Mijoz ID: ")
model = input("Mashina modeli: ")
year = int(input("Mashina yili: "))
price_per_hour = int(input("Narx (soatiga): "))
hours = int(input("Ijaraga olingan vaqt (soat): "))

# Obyektlar yaratish
customer = Customer(name, customer_id)
car = Car(model, year, price_per_hour)

# Mashinani ijaraga olish
service.rent_car(customer, car, hours)
    

