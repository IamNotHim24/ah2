people = [
    {'name':'Sumitra','age':21},
    {'name':'Tejas','age':22},
    {'name':'XYZ','age':20}
]

sorted_people = sorted(people,key=lambda x:x['age'])

print(sorted_people)