#Currency conversion

rate = float(input("Enter current exchange rate from Euro to US Dollar"))
amount =  float(input("Enter amount of currency you would like to exchange"))

usd = amount * rate
result = usd - 3.00

print(result)
