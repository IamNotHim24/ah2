try:
    with open("non_existing_file.txt","r") as file:
        data = file.read()
except FileNotFoundError as e:
    with open('error_log.txt',"a") as log_file:
        log_file.write(f'Error: {(e)}\n')
    print("error occured")