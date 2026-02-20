def is_armstrong_number(number):
    num = str(number)
    k = len(num)
    total = 0
    for arm in num:
        arm = int(arm)
        total += arm**k
    if total == number:
        return True
    else:
        return False
