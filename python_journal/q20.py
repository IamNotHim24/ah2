from collections import defaultdict
import re

def extract_emails(input_string):

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}'

    emails = re.findall(email_pattern,input_string)

    domain_classification = defaultdict(list)

    for email in emails:
        domain = email.split('@')[1]

        domain_classification[domain].append(email)


    return domain_classification

input_string = """Here are some emails: Here are some emails:
john.doe@gmail.com,
jane.doe@outlook.com,
contact@mydomain.org,
info@mydomain.org,
admin@yahoo.com,
support@yahoo.com"""

# Extract emails
classed_emails = extract_emails(input_string)
for domain,emails in classed_emails.items():
    print(f'Domain:{domain}')
    for email in emails:
        print(f'  |_{email}') 