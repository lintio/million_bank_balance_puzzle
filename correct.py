import time

TARGET = 1000000
test_days = 0
first = 1
second = 5
start = time.perf_counter()
#Day 1
balance = first
test_days += 1
print(f'Day: {test_days}, Balance: {balance}, Paid in: {first}')
#Day 2
balance += second
test_days += 1
print(f'Day: {test_days}, Balance: {balance}, Paid in: {second}')
#Day 3 bank takes over
new_bal = first + balance
last_balance = balance
balance = new_bal
test_days += 1
print(f'Day: {test_days}, Balance: {balance}')
#Bank takes over Days 4 +
while balance < TARGET:
    new_bal = last_balance + balance
    last_balance = balance
    balance = new_bal
    test_days += 1
    print(f'Day: {test_days}, Balance: {balance}')
finish = time.perf_counter()
print(f'Total Run time {round(finish-start, 2)} second(s)')