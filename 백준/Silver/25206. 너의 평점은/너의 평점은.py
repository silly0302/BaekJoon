import sys

level_grade = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

total_score = 0.0  
total_credit = 0.0  

for _ in range(20):
    title, grade, level = sys.stdin.readline().strip().split()
    grade = float(grade)

    if level == "P":
        continue  

    total_score += grade * level_grade[level]
    total_credit += grade

print(total_score / total_credit)
