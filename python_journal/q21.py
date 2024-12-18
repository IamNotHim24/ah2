import threading 
import time

def download_file(file_name):
    print(f'\nStarting download for {file_name}')
    time.sleep(2)
    print(f'\n{file_name} download completed')

files = ['f1','f2','f3']
threads = []

for file in files:
    thread = threading.Thread(target=download_file,args=(file,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()