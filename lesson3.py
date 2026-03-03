# from abc3 import Payment
# 
# class CardPayment(Payment):
#     def pay(self, amount):
#         print("Card payment", {amount})
# 
# class CryptoPayment(Payment):
#     def pay(self, amount):
#         print("Crypto payment", {amount})
# 
# def result(payment : Payment):
#     payment.pay(1000)
# 
# result(CryptoPayment())
# result(CardPayment())


# class A:
#     def heelo(self):
#         print("A")

# class B(A):
#     def heelo(self):
#         print("B")

# class C(A):
#     def heelo(self):
#         print("C")

# class D(B, C):  
#     pass

# d = D()
# d.heelo()
# print(D.__mro__)


# ЧАСТЬ 1 — Абстракция
# Создай абстрактный класс:
# User
# Требования:
# У пользователя есть:
# id
# username
# Должен быть абстрактный метод:
# get_role()
# Ты не знаешь, кто это будет — клиент, админ или курьер.
# Ты задаёшь контракт.
    
# 📌 ЧАСТЬ 2 — Инкапсуляция
# Сделай поле __balance приватным
# Добавь:
# @property balance
# метод deposit(amount)
# метод withdraw(amount)
# ⚠️ Нельзя допустить отрицательный баланс.

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @abstractmethod
    def get_role(self):
        pass

# 📌 ЧАСТЬ 3 — Наследование
# Создай классы:
# Customer
# Admin
# Courier
# Они должны наследоваться от User.
# Каждый должен реализовать:
# get_role()
# Например:
# Customer → "customer"
# Admin → "admin"
# Courier → "courier"

# 📌 ЧАСТЬ 4 — Полиморфизм
# Напиши функцию:
# def print_user_info(user: User):
# Она должна:
# выводить username
# выводить роль через user.get_role()
# Передай туда разные типы пользователей.
# Функция должна работать одинаково для всех.