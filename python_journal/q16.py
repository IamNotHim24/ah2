import re

class Validator:
    @staticmethod
    def valid_email(email):
        pattern = r'[a-zA-z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z](\.,[a-zA-Z]{2,})*$'
        return bool(re.match(pattern,email))
    
    @staticmethod
    def valid_password(password):
        return len(password)>=8
    
print(Validator.valid_email("123x@dypimr.edu.in"))
print(Validator.valid_password("Dpuimr2024"))
