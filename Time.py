from timeit import default_timer as timers

def timer(f, *args):
    start_time = timers()
    f(*args)
    end_time = timers()
    return end_time-start_time

if __name__ == '__main__':
    print(timer(zip, [1, 2, 3, 4, 5], [1, 2, 3, 4])) 
8y7t6r5e43wq	sa
