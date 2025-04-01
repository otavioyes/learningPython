from sys import getsizeof

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

#print(len(bytes(student_scores))) # 19
#print(getsizeof(student_scores)) # 216

#print(max(student_scores)) #199
#print(min(student_scores)) #24

nota = 0
for score in student_scores:
    if nota > score:
        nota = score
    print(score)