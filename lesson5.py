# class User:
#     def __init__(self, name):
#         self.name= name 

#     def hello(self):
#         print(f"hi, {self.name}")

# u1 = User("Bob")
# u1.hello()

# class User:

#     users_count = 0

#     def __init__(self, name):
#         self.name = name
#         User.users_count += 1

#     @classmethod
#     def get_users_count(cls):
#         return cls.users_count

# u1 = User("A")
# u2 = User("B")

# print(User.get_users_count())


# class MathUtils:

#     @staticmethod
#     def add(a, b):
#         print( a + b)

# obj = MathUtils()
# obj.add(2, 3)

# 
# class User:
#     def __init__(self, name):
#         self.name = name
# 
#     def __str__(self):
#         return f"User : {self.name}"
# 
# user = User("Bob")
# print(user)
# 

class Product:
    products_count = 0
    
    def __init__(self, name):
        self.name = name
        Product.products_count += 1
    
    def info(self):
        return f"Product:{self.name}"
    
    @classmethod
    def get_count(cls):
        return cls.products_count
    
    @staticmethod
    def is_valid_name(name):
        return len(name) > 2
    
    def __str__(self):
        return f"Product({self.name})"

p1 = Product("Phone")
p2 = Product("Laptop")
print(p1.info())
print(Product.get_count())
print(Product.is_valid_name("TV"))
print(p1)