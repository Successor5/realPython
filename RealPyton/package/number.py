def number(num1, num2):
    digit1 = num1 * 3
    digit2 = num2 * 2
    numbers: list = []
    digit3 = digit1 // 2
    digit4 = digit2 % digit1
    if digit4 % 2 == 0:
        numbers.append(digit4)
