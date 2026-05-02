import pandas as pd
from datetime import datetime

try:
    df = pd.read_csv(r"D:\Python_1_s\lab_7\employees.csv")
except Exception as e:
    print("Помилка відкриття CSV:", e)
    exit()

def age(date):
    birth = datetime.strptime(date, "%d.%m.%Y")
    today = datetime.today()
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

df["Вік"] = df["Дата народження"].apply(age)

try:
    with pd.ExcelWriter(r"D:\Python_1_s\lab_7\employees.xlsx", engine="openpyxl") as writer:

        df.to_excel(writer, sheet_name="all", index=False)

        df[df["Вік"] < 18][["Прізвище","Ім'я","По батькові","Дата народження","Вік"]]\
            .to_excel(writer, sheet_name="younger_18", index=False)

        df[(df["Вік"] >= 18) & (df["Вік"] < 45)][["Прізвище","Ім'я","По батькові","Дата народження","Вік"]]\
            .to_excel(writer, sheet_name="18-45", index=False)

        df[(df["Вік"] >= 45) & (df["Вік"] < 70)][["Прізвище","Ім'я","По батькові","Дата народження","Вік"]]\
            .to_excel(writer, sheet_name="45-70", index=False)

        df[df["Вік"] >= 70][["Прізвище","Ім'я","По батькові","Дата народження","Вік"]]\
            .to_excel(writer, sheet_name="older_70", index=False)

    print("Ok")

except Exception as e:
    print("Помилка створення XLSX:", e)