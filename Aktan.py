students = {}

while True:
    print("1 - Добавить студента")
    print("2 - Добавить оценку")
    print("3 - Показать журнал")
    print("4 - Выход")
    choice = input("Выбор: ")
    if choice == "1":
        name = input("Введите ФИО: ")
        if name not in students:
            students[name] = []
            print("Добавлен")
        else:
            print("Студент уже есть")
    elif choice == "2":
        name = input("Имя Фамилия: ")
        if name in students:
            try:
                grade = int(input("Оценка: "))
                students[name].append(grade)
            except:
                print("Введите число!")
        else:
            print("Нет такого студента")
    elif choice == "3":
        if students:
            for name in students:
                print(name, ":", students[name])
        else:
            print("Журнал пуст")
    elif choice == "4":
        break
    else:
        print("Неверный выбор")
