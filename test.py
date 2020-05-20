import time

TARGET = 1000000
test_days = 0
first = 154
second = 144
start = time.perf_counter()
#Day 1
balance = first
test_days += 1
print(f'Day: {test_days}, Balance: {balance}, Paid in: {first}')
#Day 2
balance += second
test_days += 1
print(f'Day: {test_days}, Balance: {balance}, Paid in: {second}')
#Day 3
bank_pays = first + balance
new_bal = balance + bank_pays
last_balance = balance
balance = new_bal
test_days += 1
print(f'Day: {test_days}, Balance: {balance}, Paid in: {bank_pays}')
#Bank takes over Days 4 +
while balance < TARGET:
    bank_pays = last_balance + balance
    new_bal = balance + bank_pays
    last_balance = balance
    balance = new_bal
    test_days += 1
    print(f'Day: {test_days}, Balance: {balance}, Paid in: {bank_pays}')
finish = time.perf_counter()
print(f'Total Run time {round(finish-start, 2)} second(s)')