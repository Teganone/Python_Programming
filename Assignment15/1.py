A1 = {
    's1': {'c1', 'c2', 'c3'},
    's2': {'c1', 'c2', 'c5'},
    's3': {'c1', 'c6', 'c2'},
    's4': {'c2', 'c6'},
    's5': {'c1', 'c2', 'c3', 'c5'},
}

A2 = {}
for student, courses in A1.items():
    for course in courses:
        if course not in A2:
            A2[course] = set()
        A2[course].add(student)

print(A2)