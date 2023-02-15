names = {'tom', 'ANNE', 'John', 'dAn'}
names = {n.capitalizwe() for n in names}
print(names)

d1 = {'a': 1, 'b':2, 'c':3}
d2 = {k*2: v*2 for k, v in d1.items()}
print(d2)

d3 = {k.upper(): v*2 for k,v in d1.items() if v % 3 == 0}
print(d3)

years = [2017,2018,2019.2020,2021]
revenues = [30000,40000,50000]
z = zip(years, revenues)
sales = list(z)
print(sales)

my_sales = dict(zip(years, revenues))
print(my_sales)

profit = {k: v*0.15 for k,v in my_sales.items()}
print(profit)
