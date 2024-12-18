def compound_interest(principal,rate,time,frequency):
    amount = principal

    def calculate_interest():
        nonlocal amount
        amount = principal * (1 + rate/frequency)**(frequency*time)
    calculate_interest()
    return amount

print(compound_interest(1000,0.05,5,4))