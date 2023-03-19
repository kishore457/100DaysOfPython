student_scores = input("Input a list of student scores").split()
for i in range(0,len(student_scores)):
    student_scores[i] =  int(student_scores[i])
max =0

for j in student_scores:
    if j > max:
        max =j
print(f"The highest score in the class is: {max}")











