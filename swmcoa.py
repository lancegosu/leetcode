# Input string
strrates = "5.0,100,5.5,90,6.0,91:L10;5.0,101,5.5,95,6.0,97:L20;"

lockperiods = strrates.split(';')[:-1]
print(lockperiods)

locks = []
rates_prices = {}

# parsing
for period in lockperiods:
    data = period.split(':')
    locks.append(data[-1])
    numbers = data[0].split(',')
    # print(numbers)

    # creating the data structure
    for i, num in enumerate(numbers):
        # print(i, num)
        if i % 2 == 0:
            rate = num
        else:
            price = num
            prices = rates_prices.get(rate, [])
            prices.append(price)
            rates_prices[rate] = prices

print(' ' + ', '.join(locks))

for row in rates_prices:
    print('[' + row + ',', ', '.join(rates_prices[row]) + ']')