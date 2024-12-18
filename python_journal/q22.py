import threading

def print_even():
    lock = threading.Lock()
    with lock:
        for i in range(0,12,2):
            print(f'Even : {i}\t')

def print_odd():
    lock = threading.Lock()
    with lock:
        for i in range(1,12,2):
            print(f'Odd : {i}\t')

eve_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

eve_thread.start()
odd_thread.start()

eve_thread.join()
odd_thread.join()