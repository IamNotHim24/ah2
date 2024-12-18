class AgeException(Exception):
    pass

def valid_age(age):
    if age<0 or age>100:
        raise AgeException("Invalid age it should be greater than 0 and less than 100")
    print(age,' is valid')

try:
    valid_age(-69)
except AgeException as e:
    print(e)