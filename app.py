from numpy import median

from students import students
from utils.helpers import highest_score, lowest_score, average_score

highest = highest_score(students)
lowest = lowest_score(students)
average = average_score(students)

print("Current Students:", students)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)

print(f"{'Name':<10}{'Score':>6}")
for s in students:
    print(f"{s['name']:<10}{s['score']:>6}")
print(f"\nHighest : {highest}\nLowest  : {lowest}\nAverage : {average:.1f}\nMedian  : {median}")