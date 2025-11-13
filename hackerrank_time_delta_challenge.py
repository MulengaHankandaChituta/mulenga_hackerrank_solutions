# time_delta_problem.py

from  datetime import datetime

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    diff = abs(int((dt1 - dt2).total_seconds()))
    return str(diff)

if __name__== '__main__':
    t = int(input("Enter number of test case: "))
    for _ in range(t):
        t1 = input("Enter first timestamp: ").strip()
        t2 = input("Enter second timestamp: ").strip()
        print(time_delta(t1, t2))
