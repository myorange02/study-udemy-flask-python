# def add(x, y):
#     return x + y

# add = lambda x, y: x + y
# print((lambda x, y: x + y)(1, 2))

sequence = [1, 3, 5, 9]
doubled = [(lambda x : x * 2)(x) for x in sequence]
print(doubled)