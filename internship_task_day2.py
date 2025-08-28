# Internship Task - Day 2
# Arithmetic Operators and Variables
# --------------------------------------------------

# Q1: Calculate the multiplication and sum of two numbers
print("Q1 Output:")
a, b = 6, 3
print("Numbers:", a, b)
print("Sum =", a + b)
print("Multiplication =", a * b)
print("-" * 40)

# Q2: Create a string made of the first, middle and last character
print("Q2 Output:")
text = "Quality Thought"
first = text[0]
middle = text[len(text) // 2]
last = text[-1]
print("Original String:", text)
print("First + Middle + Last =", first + middle + last)
print("-" * 40)

# Q3: One half of 100 is 50 (using variable)
print("Q3 Output:")
num = 100
half = num // 2
print("One half of", num, "is", half)
print("-" * 40)

# Q4: myTotal = 4 + 2 * 8 - 6
print("Q4 Output:")
myTotal = 4 + 2 * 8 - 6
print("myTotal =", myTotal)
print("Explanation: Multiplication has higher precedence → 4 + (16) - 6 = 14")
print("-" * 40)

# Q5: Floor division
print("Q5 Output:")
myTotal = 7 // 5
print("7 // 5 =", myTotal, "(Floor division gives integer result)")
print("-" * 40)

# Q6: Using parentheses
print("Q6 Output:")
myTotal = (8 + 2) * 10
print("(8 + 2) * 10 =", myTotal)
print("-" * 40)

# Q7: Operator precedence without parentheses
print("Q7 Output:")
myTotal = 8 + 2 * 10
print("8 + 2 * 10 =", myTotal, "(Because 2*10=20, then 8+20=28)")
print("-" * 40)

# Q8: Division with and without parentheses
print("Q8 Output:")
myTotal1 = 8 + 10 / 2
myTotal2 = (8 + 10) / 2
print("8 + 10 / 2 =", myTotal1)
print("(8 + 10) / 2 =", myTotal2)
print("-" * 40)

# Q9: Using variables with operations
print("Q9 Output:")
numberOne, numberTwo = 16, 4
answer1 = numberOne + numberTwo + 20
answer2 = 10 * numberOne + (numberTwo + 20)
answer3 = numberOne + 20 + numberTwo - 10
print("numberOne =", numberOne, ", numberTwo =", numberTwo)
print("answer1 =", answer1)
print("answer2 =", answer2)
print("answer3 =", answer3)
print("-" * 40)

# Q10: String concatenation
print("Q10 Output:")
FirstName = "Quality"
SecondName = "Thought"
full_name = FirstName + " " + SecondName
print("Full Name is:", full_name)
print("-" * 40)
