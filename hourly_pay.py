"""
This program takes in user input for hours worked and overtime hours worked. It then uses a conditional
to determine if hours are 40 or less which issues regular pay and if hours exceed that the overtime value is
calculated and printed.
"""

hrs = float(input("Enter hours worked: "))
ot_hrs=float(input("Enter overtime: "))
rate = 10.5
reg_pay = 10.5 * hrs
ot_rate = rate * 1.5
ot_pay = ot_rate * ot_hrs
tot_ot = reg_pay + ot_pay

if hrs + ot_hrs <= 40:
	print(reg_pay)
else:
	print(tot_ot)


