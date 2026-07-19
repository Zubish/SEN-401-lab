def highest_score(students):
    return max(students, key=lambda student: student["score"])


def lowest_score(students):
    return min(students, key=lambda student: student["score"])


def average_score(students):
    total = sum(student["score"] for student in students)
    return total / len(students)

def average_score(data):
    if len(data) == 0:
        return 0  # Corrective fix: avoid ZeroDivisionError on empty list
    total = sum(d["score"] for d in data)
    return total / len(data)