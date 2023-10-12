tickets = int(input("Количество билетов : "))
tickets_1 = tickets
b_age = {}
amount = 0
while tickets > 0:
    Age = int(input("Возраст покупателя : "))
    b_age[tickets] = Age
    tickets = tickets - 1
b_age_items = b_age.items()
for [b_name, age] in b_age_items:
    if 18 <= age <= 25:
        amount = amount + 990
    elif 18 > age:
        amount = amount + 0
    elif age > 25:
        amount = amount + 1390
if tickets_1 > 3:
    amount = amount - amount * 0.1
amount = str(amount)
print ('Сумма к оплате: ' + (amount))