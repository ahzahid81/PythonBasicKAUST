origprice = float(input('Enter the original price: $'))
discount = float(input('Enter the discount percentage: '))

newPrice = (1 - discount/100)*origprice
calculation = '${} discounted by {}% is ${}'.format(origprice, discount, newPrice)

print(calculation)
