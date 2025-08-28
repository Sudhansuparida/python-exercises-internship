# Internship Task - Day 5
# Variables, Data Types, Logical, Membership and Identity Operators
# --------------------------------------------------

# Q1: Swapping values
print("Q1 Output:")
x, y = 10, 5
print("Before swapping:", "x =", x, ", y =", y)
x, y = y, x
print("After swapping:", "x =", x, ", y =", y)
print("-" * 40)

# Q2: Number types
print("Q2 Output:")
a = 855               # int
b = 2.564728          # float
c = 2 + 3j            # complex
print("Integer:", a, "Type:", type(a))
print("Float:", b, "Type:", type(b))
print("Complex:", c, "Type:", type(c))
print("-" * 40)

# Q3: Output of given code
print("Q3 Output:")
x = 6
y = 2
print(x ** y)   # 6^2 = 36
print(x // y)  # Floor division = 3
print("-" * 40)

# Q4: Bitwise operators
print("Q4 Output:")
a = 4    # binary: 0100
b = 11   # binary: 1011
print(a | b)   # bitwise OR → 15
print(a >> 2)  # right shift 2 → 1
print("-" * 40)

# Q5: Assignment operator
print("Q5 Output:")
y = 10
# NOTE: "x = y += 2" is INVALID syntax in Python, it raises SyntaxError.
# Correct usage:
y += 2
x = y
print("x =", x)  # 12
print("-" * 40)

# Q6: Expression
print("Q6 Output:")
print(2 * 3 ** 3 * 4)  # 2 * 27 * 4 = 216
print("-" * 40)

# Q7: Expression
print("Q7 Output:")
print(10 - 4 * 2)  # 10 - 8 = 2
print("-" * 40)

# Q8: Expression
print("Q8 Output:")
print(-18 // 4)  # Floor division: -5
print("-" * 40)

# Q9: Logical operators
print("Q9 Output:")
x = 10
y = 50
if x ** 2 > 100 and y < 100:   # 100 > 100? No → False, so nothing prints
    print(x, y)
print("No output (condition false)")
print("-" * 40)

# Q10: Logical AND
print("Q10 Output:")
x = 100
y = 50
print(x and y)  # returns y (50) because both are truthy
print("-" * 40)

# Q11: type(range(5))
print("Q11 Output:")
print(type(range(5)))  # <class 'range'>
print("-" * 40)

# Q12: Data type of type(10)
print("Q12 Output:")
print(type(10))        # int
print(type(type(10)))  # <class 'type'>
print("-" * 40)
