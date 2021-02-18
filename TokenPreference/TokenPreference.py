def PopularTopic(topics):
    max = int(topics[0][1])
    maxIndex = 0
    for Topic in range(len(topics)):
        if int(topics[Topic][1]) > max:
            max = int(topics[Topic][1])
            maxIndex = Topic
    return maxIndex

StudentTeamStatus = {    
}

Settings = open("Settings.txt", "r")
reader = Settings.readlines()
i = 0
while reader[i] != "Topics\n":
    if i == 1:
        for word in reader[i].split():
            if word.isdigit():
                MaxSize = int(word)
    #Add More Ifs here if there are more settings that need to be added
    i += 1

topics = []
while reader[i] != "Participants/Token Distribution\n":
    if reader[i] != "" and reader[i] != "Topics\n" and reader[i] != '\n':
        reader[i] = reader[i][:-1]
        topic = []
        topic.append(reader[i])
        topic.append(0)
        topics.append(topic)
    i += 1

i += 1
students = []
while reader[i] != "END\n":
    if reader[i] != "" and reader[i] != "\n":
        student = []
        x = -1
        for word in reader[i].split():
            student.append(word)
            if x != -1:
                topics[x][1] += int(word)
            x += 1
        students.append(student)
        StudentTeamStatus.update({f"{student[0]}": "No Team"})
    i += 1

for Topic in range((len(students)//MaxSize) + 1):
    x = PopularTopic(topics)
    print(topics[x])
    members = 0
    for it in range(len(topics)):
        for S in range(len(students)):
            if int(students[S][x + 1]) == len(topics) - it and StudentTeamStatus[students[S][0]] != "Has Team":
                StudentTeamStatus.update({f"{students[S][0]}": "Has Team"})
                print(f"{students[S][0]} : {students[S][x + 1]}")
                members += 1
            if members == MaxSize:
                break;
        if members == MaxSize:
            break;
    print("")
    topics[x][1] = 0


for Student in StudentTeamStatus:
    if(StudentTeamStatus[Student] == "Has Team"):
        print(Student + ' : ' + StudentTeamStatus[Student])

for Student in StudentTeamStatus:
    if(StudentTeamStatus[Student] == "No Team"):
        print(Student + ' : ' + StudentTeamStatus[Student])

Settings.close()