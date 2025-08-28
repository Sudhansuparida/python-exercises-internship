# Internship Task - Day 3
# Relational and Assignment Operators
# --------------------------------------------------

# Q1
print("Q1 Output:")
print(2 ** 3 ** 2)  # Exponentiation is right-to-left: 3**2=9, then 2**9=512
print("-" * 40)

# Q2
print("Q2 Output:")
print(2 * 3 ** 3 * 4)  # 3**3=27, then 2*27*4=216
print("-" * 40)

# Q3
print("Q3 Output:")
print(10 - 4 * 2)  # 4*2=8, then 10-8=2
print("-" * 40)

# Q4
print("Q4 Output:")
print(-18 // 4)  # Floor division: -18/4=-4.5 -> floor = -5
print("-" * 40)

# Q5
print("Q5 Output:")
print(2 % 6)  # Remainder: 2
print("-" * 40)

# Q6
print("Q6 Output:")
x, y = 100, 50
print(x and y)  # Returns second operand since both are True → 50
print("-" * 40)

# Q7
print("Q7 Output:")
print(36 / 4)  # Division → 9.0
print("-" * 40)

# Q8
print("Q8 Output:")
var1, var2, var3 = 1, 2, "3"
# The below line would cause error (int + str), so we show explanation
try:
    print(var1 + var2 + var3)  # Will cause TypeError
except TypeError:
    print("Error: cannot add int and string directly (1+2+'3').")
print("If we convert var3 to int, result would be:", var1 + var2 + int(var3))
print("-" * 40)

# Q9
print("Q9 Output:")
p, q, r = 10, 20, 30
print(p, q, r)
print("-" * 40)

# Q10
print("Q10 Output:")
valueOne = 5 ** 2
valueTwo = 5 ** 3
print(valueOne)  # 25
print(valueTwo)  # 125
print("-" * 40)

# Q11
print("Q11 Output:")
var = "James" * 2 * 3
print(var)  # "James" * 6 = "JamesJamesJamesJamesJamesJames"
print("-" * 40)

# Q12
print("Q12 Output:")
x = 36 / 4 * (3 + 2) * 4 + 2
print(x)  # 36/4=9, (3+2)=5 → 9*5*4+2=182
print("-" * 40)

# Q13
print("Q13 Output:")
print(type(10))  # <class 'int'>
print("-" * 40)

# Q14
print("Q14 Output:")
int_var = 42
float_var = 3.14
string_var = "Hello Python"
print("int_var =", int_var, "| Type:", type(int_var))
print("float_var =", float_var, "| Type:", type(float_var))
print("string_var =", string_var, "| Type:", type(string_var))
print("-" * 40)

# Q15
print("Q15 Output:")
roll_number = 33
print("Roll number is:", roll_number)
print(type(roll_number))
num = 25
print(num)
print(type(num))
print("-" * 40)
