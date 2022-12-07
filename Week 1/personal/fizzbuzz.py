#fizzbuzz game
#divisible by 3, print fizz
#divisible by 5, print buzz
#divisible by both, print fizzbuzz
# if divisible by none, print the number

# solution:
# 1. for number input, we use for loop
# 2. 4 conditional statements for checking divisibility


for i in range(100):
    # modulo operator (%) -> remainder
    if i % 5 == 0 and i % 3 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)