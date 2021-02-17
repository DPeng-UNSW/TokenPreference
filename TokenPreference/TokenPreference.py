import sys

nTopics = input("How many topics are there?\n")
topics = []
tokens = []
for x in range(int(nTopics)):
    x = input(f"Enter topic {x + 1}:\n")
    topics.append(x)
    tokens.append(int(0))
nStudents = input("How many students are there?\n")
students = []

print("List Them:")
for x in range(int(nStudents)):
    x = input();
    student = []
    student.append(x)
    students.append(student)
    print("Tokens for Topic :")
    for j in range(int(nTopics)):
        y = input(f"{topics[j]}\n")
        num = int(y)
        student.append(int(y))
        tokens[j] += num

sortedTokens = sorted(tokens)
for i in range(3):
    for j in range(int(nTopics)):
        if(sortedTokens[i] == tokens[j]):
            print(f"Topic chosen : {topics[j]}")
            for x in range(int(nStudents)):
                if students[x][j] != 0:
                    print(f"{students[x][0]} : {students[x][j]}")
            tokens[j] = -1
            break



    