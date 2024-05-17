import random

class Student:

    def __init__(self, full_name, gender):
        self.full_name = full_name
        self.gender = gender

class User:

    def __init__(self, name, comments=0, likes=0, online=False):
        self.name = name
        self.comments = comments
        self.likes = likes
        self.online = online

    def talk(self):
        print("Моє ім'я:", self.name)

    def _comments(self, num_comments):
        self.comments += num_comments

    def _likes(self, num_likes):
        self.likes += num_likes

    def share_(self):
        print(f"{self.name} поділився постом")

    def online_status(self, status):
        self.online = status

    def __str__(self):
        return f"Об'єкт класа User\nім'я: {self.name}\nкоментарі: {self.comments}\nлайки: {self.likes}\nонлайн: {self.online}"

class Television:

    def __init__(self):
        self.channel = 33
        self.volume = 82

    def change_channel(self, channel):
        if 1 <= channel <= 100:
            self.channel = channel
        else:
            print("Неприпустимий номер каналу")

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Максимальний рівень гучності")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Мінімальний рівень гучності")

    def __str__(self):
        return f"Канал: {self.channel}, Гучність: {self.volume}"

if __name__ == "__main__":
    students = [
        Student("Іванов Антон Іванович", "Чоловіча"),
        Student("Гордіїв Петро Петрович", "Чоловіча"),
        Student("Сидорова Катерина Василівна", "Жіноча"),
        Student("Ковальова Марія Вікторівна", "Жіноча"),
        Student("Смирнов Сергій Андрійович", "Чоловіча"),
        Student("Василенко Анна Ігорівна", "Жіноча"),
        Student("Клименко Олександр Михайлович", "Чоловіча"),
        Student("Михайленко Тетяна Олександівна", "Жіноча"),
        Student("Бондаренко Максим Павлович", "Чоловіча"),
        Student("Литвиненко Людмила Валентинівна", "Жіноча"),
    ]

    users = [
        User('Яна', random.randint(0, 10), random.randint(0, 20)),
        User('Нікіта', random.randint(0, 10), random.randint(0, 20))
    ]

    while True:
        print("\nМеню:")
        print("1. Робота зі студентами")
        print("2. Робота з користувачами сайту")
        print("3. Робота з телевізором")
        print("4. Змінити статус онлайн/офлайн")
        print("5. Вихід")
        a = input("Оберіть опцію: ")

        if a == "1":
            print("\nСписок студентів:")
            for student in students:
                print(student.full_name, "-", student.gender)
        elif a == "2":
            print("\nСписок користувачів сайту:")
            for user in users:
                print(user)
            action = input("Введіть 'к', щоб додати коментарі, 'л', щоб додати лайки, 'п', щоб поділитися постом: ")
            if action == 'к':
                num_comments = int(input("Введіть кількість коментарів, які потрібно додати: "))
                for user in users:
                    user._comments(num_comments)
            elif action == 'л':
                num_likes = int(input("Введіть кількість лайків, які потрібно додати: "))
                for user in users:
                    user._likes(num_likes)
            elif action == 'п':
                for user in users:
                    user.share_()
        elif a == "3":
            tv = Television()
            while True:
                print("\nМеню телевізора:")
                print("1. Змінити канал")
                print("2. Збільшити гучність")
                print("3. Зменшити гучність")
                print("4. Вимкнути телевізор")
                tv_choice = input("Оберіть опцію: ")
                if tv_choice == "1":
                    channel = int(input("Введіть номер каналу: "))
                    tv.change_channel(channel)
                elif tv_choice == "2":
                    tv.increase_volume()
                elif tv_choice == "3":
                    tv.decrease_volume()
                elif tv_choice == "4":
                    break
                print(tv)
        elif a == "4":
            for user in users:
                user.online_status(not user.online)
                print(f"Статус користувача {user.name} змінено на {('онлайн' if user.online else 'офлайн')}")
        elif a == "5":
            break
