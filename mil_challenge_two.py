import concurrent.futures
import time

start = time.perf_counter()

TARGET = 1000000
temp_success = []
Success = [0, TARGET, TARGET]

#split target 1%
range_end = int(TARGET / 100) #TARGET - int((TARGET / 100) * 99)
loop_start = []
loop_end = []
first_deposit = []
loop_start.append(1)
loop_end.append(int(range_end / 10))
for x in range(1, 10):
    loop_start.append(int(((range_end / 10) * x)))
    loop_end.append(int((range_end / 10) * (x + 1)))

for idx, start_point in enumerate(loop_start):
    first_deposit.append((start_point, loop_end[idx]))
#print(first_deposit)

def calculate(first_deposit):
    #calc_start = time.perf_counter()
    #print(f'Starting Caluclations {first_deposit}')
    minor_success = [0, TARGET, TARGET]
    for i in range(first_deposit[0], first_deposit[1]):
        for x in range(1, range_end):
            days = 0
            init_a_deposit = i
            init_b_deposit = x
            #Day 1
            balance = init_a_deposit
            days += 1
            #Day 2
            balance += init_b_deposit
            days += 1
            #Day 3
            new_bal = init_a_deposit + balance
            last_balance = balance
            balance = new_bal
            days += 1
            #Bank takes over Days 4 +
            if balance > TARGET:
                continue
            while balance < TARGET:
                new_bal = last_balance + balance
                last_balance = balance
                balance = new_bal
                days += 1
            if balance == TARGET:
                if days == max(days, minor_success[0]):
                    minor_success = [days, init_a_deposit, init_b_deposit]
    #calc_finish = time.perf_counter()
    #print(f'Finished Caluclations {first_deposit} in {round(calc_finish-calc_start, 2)}')
    return(minor_success)

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        print('Running...')
        results = executor.map(calculate, first_deposit)
    
    print('Finishing Up...')
    for r in results:
        temp_success.append(r)

    for result in temp_success:
        #print(result, Success)
        if result[0] == max(result[0], Success[0]):
            Success = result
    finish_pt1 = time.perf_counter()
    print(f'All calculatons took {round(finish_pt1-start, 2)} second(s). The best result is {Success}')
    print(f'Running calculations to show full result \nusing {Success[1]} as first deposit and {Success[2]} as second deposit')
    test_days = 0
    #Day 1
    balance = Success[1]
    test_days += 1
    print(f'Day: {test_days}, Balance: {balance}, Paid in: {Success[1]}')
    #Day 2
    balance += Success[2]
    test_days += 1
    print(f'Day: {test_days}, Balance: {balance}, Paid in: {Success[2]}')
    #Day 3
    new_bal = Success[1] + balance
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
    print(f'Single Calculation took {round(finish-finish_pt1, 2)} second(s)\nTotal Run time {round(finish-start, 2)} second(s)')
