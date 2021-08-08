last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# Your code below: 
gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]

gradebook.append(["Computer Science", 100])
gradebook.append(["Visual Arts", 93])
gradebook[5][1] = gradebook[5][1] + 5
gradebook[2].remove(85)
gradebook[2].append("Pass")

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)