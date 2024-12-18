set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1.copy()

for elem in set2:
        union_set.add(elem)
print(union_set)

intersection_set = {elem for elem in set1 if elem in set2}

print(intersection_set)


diff_set = set()

for elem in set1:
        if elem not in set2:
                diff_set.add(elem)

for elem in set2:
        if elem not in set1:
                diff_set.add(elem)

print(diff_set)