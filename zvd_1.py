import csv 
import random 
from faker import Faker 
from datetime import datetime 

 

fake = Faker('uk_UA') 
 

male_patronymics = [
    "Геннадійович", "Арсенович", "Вадимович", "Павлович", "Михайлович",
    "Юрійович", "Степанович", "Євгенович", "Романович", "Ігорович",
    "Олександрович", "Денисович", "Костянтинович", "Тарасович", "Сергійович",
    "Васильович", "Федорович", "Володимирович", "Антонович", "Олегович",
    "Богданович", "Леонідович", "Андрійович", "Ярославович", "Дмитрович",
    "Русланович", "Петрович", "Максимович", "Станіславович", "Іванович",
    "Миколайович", "Григорович", "Едуардович", "Віталійович", "Олексійович"
]

 
female_patronymics = [
    "Григорівна", "Арсенівна", "Юріївна", "Василівна", "Петрівна",
    "Максимівна", "Олександрівна", "Ігорівна", "Степанівна", "Романівна",
    "Сергіївна", "Миколаївна", "Дмитрівна", "Богданівна", "Андріївна",
    "Володимирівна", "Олегівна", "Тарасівна", "Іванівна", "Павлівна"
]
 

jobs = ["Менеджер", "Бухгалтер", "Програміст", "Адміністратор", "Інженер"] 


with open("D:\Python_1_s\lab_7\employees.csv", "w", newline="", encoding="utf-8") as file: 
    writer = csv.writer(file) 
    writer.writerow([ 
        "Прізвище","Ім'я","По батькові","Стать","Дата народження", 
        "Посада","Місто","Адреса","Телефон","Email" 
    ]) 

 

    for i in range(500): 
        gender = "Жіноча" if i < 200 else "Чоловіча" 

        if gender == "Жіноча": 
            last = fake.last_name_female() 
            first = fake.first_name_female() 
            father = random.choice(female_patronymics) 
        else: 
            last = fake.last_name_male() 
            first = fake.first_name_male() 

        birth = fake.date_between( 
            start_date=datetime(1946,1,1), 
            end_date=datetime(2011,12,31) 
        ) 

        writer.writerow([ 
            last, 
            first, 
            father, 
            gender, 
            birth.strftime("%d.%m.%Y"), 
            random.choice(jobs), 
            fake.city(), 
            fake.address().replace("\n", " "), 
            fake.phone_number(), 
            fake.email() 
        ]) 
 
print("Ok") 