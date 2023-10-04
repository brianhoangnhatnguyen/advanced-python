the_Dictionary = {'Name': ['Andrew', 'Sarah', 'Nathan'], 'Age': 14, 'ID': 187345}
print(the_Dictionary['Name'])

the_Dictionary['Age'] = '15'
print(the_Dictionary['Age'])

the_Dictionary['City'] = 'NY'
print(the_Dictionary)

print("")

student_scores = [{'Name': 'Bob', 'Score': [90, 88, 95]},
                  {'Name': 'Ryan', 'Score': [87, 85, 91]},
                  {'Name': 'John', 'Score': [95, 90, 89]}
                  ]

average_scores = {}

for student in student_scores:
    studentName = student['Name']
    studentScore = student['Score']
    averageScore = sum(studentScore) / len(studentScore)
    average_scores[studentName] = averageScore

print(average_scores)