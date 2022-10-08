# def print_hello(name, age, grade=0):
#     return f"{name} your age is {age} and you got {grade}"
#
#
# x = print_hello(name='Xcho', age=26, grade=4)
# y = print_hello(age=17, name='Arman')
#

# print(x, y)


# def creat_list(*args):
#     list = []
#     for i in args:
#         list.append(i)
#     return list
#
#
# creat_list.append("go")
#
# print(creat_list('apple', 68))
# def creat_dict(**kwargs):
#     return kwargs
#
#
# x = creat_dict(fruit='apple', gin=68)
# print(x)
#
# def func(pos_arg, def_arg=None, *args, **kwargs):
#     pass
#
# def x(*args):
#     print("Printing values")
#     for i in args:
#         print(i)
#     return args
#
#
# c = x(20, 40, 60)
# y = x(80, 100)
# def calculation(name, num=9000):
#     return name, num
#
#
# x = calculation("Ben", 12000)
# y = calculation("Jessa")
# print(x, y)
# outer function
# def outer_fun(a, b):
#     square = a ** 2
#
#     # inner function
#     def addition(a, b):
#         return a + b
#     add = addition(a, b)
#     return add + 5
# result = outer_fun(5, 10)
# print(result)
# 1-------------------
# def addition(num):
#     if num:
#         return num + addition(num - 1)
#     else:
#         return 0
#
#
# x = addition(10)
# print(x)
#
# def y(name, age):
#     print(name, age)
#
#
# y("Emma", 26)
# x = y
#
# x("Arman", 25)
# 2---------------------
# print(list(range(4, 30, 2)))
# for i in range(4, 30, 2):
#     print(i, end=" ")
# 3--------
# 0____________
# def x(num):
#     for i in range(0, num + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('Buzz', 'fizz')
#         elif i % 3 == 0:
#             print('Buzz')
#         elif i % 5 == 0:
#             print("fizz")
#         else:
#             print(i)
#
#
# x(100)
# ==============
# x = [4, 6, 8, 24, 12, 2]
# print(max(x))
# =============
# x = [4, 5, 88, -34, 66]
# print(min(x))
# ============
# def x(str):
#     return str[::-1]
#
#
# print(x("a b c"))
# =======================
# x = ["bob", "likes", "dogs"]
# x.reverse()
# print(x)
# ========================
# def works_for_all(func):
#     def inner(*args, **kwargs):
#         print("I can decorate any function")
#         return func(*args, **kwargs)
#     return inner
#
#
# @works_for_all
# def creat_list(*args):
#     list = []
#     for i in args:
#         list.append(i)
#     return list[::-1]
#
#
# print(creat_list("bob", "likes", "dogs"))
# =========================
# x = [1, 3, 5, 3, 7, 3, 1, 1, 5]
# y = []
#
# for i in x:
#     if i not in y:
#         y.append(i)
#
# print("Patasxan")
# for i in y:
#     print(i, end=" ")
# list = [1, 2, 3, 4, 3, 2, 3, 4]
#
# y = {}
# for i in list:
#     y[i] = y.get(i, 0)+1
# print(y)
# ==================
# def make_pretty(func):
#     def inner():
#         print("i got decorated")
#         func()
#     return inner
#
#
# @make_pretty
# def normal():
#     print("i am normal")
#
#
# normal()
# def smart_divide(func):
#     def inner(a, b):
#         if b == 0:
#             print("chem tpi")
#             return
#         print("hesa kbajani")
#         func(a, b)
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
#
# divide(5.9, -95)
# def works_for_all(func):
#     def inner(*args, **kwargs):
#         print("I can decorate any function")
#         return func(*args, **kwargs)
#     return inner
#
# def (func):
#     def inner():
#         print("i got decorated")
#         func()
#     return inner
#
# @star
# @percent
# def printer(msg, another_messegae):
#     print(msg, "myus", another_messegae)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# *****************************
# printer
# *****************************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def star(func):
    def inner(*args, **kwargs):
        print("%" * 20)
        func(*args, **kwargs)
        print("%" * 20)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("*" * 20)
        func(*args, **kwargs)
        print("*" * 20)
    return inner


@star
@percent
def printer(msg, another_messegae):
    print(msg, "my little", another_messegae)


printer("Hello,", "man")
