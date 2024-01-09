grade1 = [8.5, 8.0, 7.0, 6.5, 5.5, 5.0, 4.0, 0]
grade2 = ['A','B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
grade3 = [4.0, 3.5, 3, 2.5, 2, 1.5, 1, 0]
grade = float(input("Enter your grade: "))
pos = 0
while grade1[pos] > grade:
    pos += 1
print("Grade letter: ", grade2[pos])
print("Grade (4): ", grade3[pos])
