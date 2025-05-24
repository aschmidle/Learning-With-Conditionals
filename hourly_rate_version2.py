hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))


if hrs > 40:
    print("Overtime")
    reg_pay = hrs*rate
    ot = (hrs - 40) * (rate * .5)
    print(reg_pay + ot)
else:
    print("Regular Pay")
    reg_pay = hrs*rate
    print(reg_pay)
