name = input("Введите название товара: ")
price = float(input("Введите цену товара: "))
quantity = int(input("Введите количество товара: "))

total = price * quantity

if total >= 15000:
    discount = 15
elif total >= 10000:
    discount = 10
elif total >= 5000:
    discount = 5
else:
    discount = 0

discount_money = total * discount / 100
final_price = total - discount_money

print("\n--- Чек ---")
print("Товар:", name)
print("Исходная стоимость:", total, "руб.")
print("Скидка:", discount, "%")
print("Скидка в рублях:", discount_money, "руб.")
print("Итоговая стоимость:", final_price, "руб.")

# Дополнительный функционал
if discount > 0:
    print("Вы сэкономили:", discount_money, "руб.")
else:
    print("Для получения скидки купите товаров на сумму от 5000 руб.")

if final_price >= 20000:
    print("Большая покупка!")

answer = input("Хотите рассчитать ещё одну покупку? (да/нет): ")

if answer == "да":
    print("Запустите программу ещё раз.")
else:
    print("Спасибо за использование программы!")
