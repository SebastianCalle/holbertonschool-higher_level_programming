#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(.9999999999999999999, .99999999))
print(add_integer(.222222222, .99999999))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer("School", 3))
except Exception as e:
    print(e)
try:
    print(add_integer())
except Exception as e:
    print(e)
try:
    print(add_integer([1, 2]))
except Exception as e:
    print(e)
try:
    print(add_integer(2, [2, 3]))
except Exception as e:
    print(e)
