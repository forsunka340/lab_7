import pandas as pd
import matplotlib.pyplot  as plt
from datetime import datetime

#Завантаження даних
try:
    df = pd.read_csv(r"D:\Python_1_s\lab_7\employees.csv")
    print("Дані успішно завантажено")
except Exception as e:
    print("Помилка відкриття CSV:", e)
    exit()


#Розрахунок віку
def calc_age(birth_date):
    birth = datetime.strptime(birth_date, "%d.%m.%Y")
    today = datetime.today()
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


df["Вік"] = df["Дата народження"].apply(calc_age)


#Функції для груп
def get_group(dataframe, group_name):
    if group_name == "younger_18":
        return dataframe[dataframe["Вік"] < 18]
    elif group_name == "18-45":
        return dataframe[(dataframe["Вік"] >= 18) & (dataframe["Вік"] < 45)]
    elif group_name == "45-70":
        return dataframe[(dataframe["Вік"] >= 45) & (dataframe["Вік"] < 70)]
    else:
        return dataframe[dataframe["Вік"] >= 70]


#Стать
gender_counts = df["Стать"].value_counts()

print("Розподіл за статтю:")
print(gender_counts)

gender_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Стать працівників")
plt.ylabel("")
plt.show()


#Вікові групи
groups = {
    "younger_18": get_group(df, "younger_18"),
    "18-45": get_group(df, "18-45"),
    "45-70": get_group(df, "45-70"),
    "older_70": get_group(df, "older_70")
}

group_sizes = {k: len(v) for k, v in groups.items()}

print("\nКількість у вікових групах:")
print(group_sizes)

plt.bar(group_sizes.keys(), group_sizes.values())
plt.title("Вікові категорії")
plt.show()


#Стать всередині груп
for name, subset in groups.items():
    gender_in_group = subset["Стать"].value_counts()

    print(f"\nГрупа: {name}")
    print(gender_in_group)

    gender_in_group.plot(kind="bar")
    plt.title(f"Стать у групі {name}")
    plt.show()