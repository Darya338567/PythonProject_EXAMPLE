class Bird:
    wings = True
    beak = True
    plumage = True

    """Функции внутри классов = методы"""

    def fly(self):
        print("Машу крыльями, лечу")

    """Создаем заглушку метода: то есть, данный метод применим к любому подклассу класса Bird, но описать его надо отдельно"""
    def walk(self):
        pass

class Sparrow(Bird):
    size = "small"

    """Описали подметод"""
    def walk(self):
        print("Прыг-прыг")

"""Создаем объекты класса, то есть объект, соответствующий описанию класса. Свойство объекта изменяемо.."""
chizhik = Sparrow()
chizhik.size = "medium"
pyzhyk = Sparrow()
print(chizhik.beak)
print(chizhik.size)
pyzhyk.walk()
print(chizhik.wings)

"""Подклассы имеют доступы только к свойствам и методам родительского класса, но не другого подкласса"""


