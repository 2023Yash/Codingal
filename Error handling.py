# try:
#     n = [1, 3] + [2, 4]
# except TypeError:
#     print("Type error")
# except:
#     print("normal error")
# else:
#     print("no error")

# x = 1
# y = 2
# if x != y:
#     raise ArithmeticError("Numbers are not Equal")

def func(x):
    x += func(x)

func("abc")