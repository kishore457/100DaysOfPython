# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# we have len() and sum() function for calculating the lenght and sum of elements in the list.
length = 0
for i in student_heights:
    length += 1
# print(length)

height_sum = 0
for n in student_heights:
    height_sum += n
# print(height_sum)

height_avg = round(height_sum/length)
print(height_avg)




