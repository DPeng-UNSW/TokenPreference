#Define Certain Settings
Max_Team_Size = 4
Min_Team_Size = 3

Topics = ["Machine Learning", "Organ Exchange", "Degree Planner", "Differential Privacy", "Random Sampling", "Visualization", "Benchmark Graph Instances", "Graph Theory in Finance", "Enumeration Algorithms"]

#Get Topics
Topics_Membership = {}
for Topic in Topics:
    Topics_Membership.update({Topic: {}})

#Get Students
def add_student(Name, preferences, topics, student_Dictionary):
    Student_Preferences = {}
    for topic in range(len(preferences)):
        Student_Preferences.update({topics[topic]: preferences[topic]})
    student_Dictionary.update({Name: Student_Preferences})
    return Student_Preferences


Students = { }
add_student("David Peng", [3, 2, 1, 0, 2, 0, 0, 0, 0], Topics, Students)
add_student("Jodie Lee", [1, 1, 1, 1, 3, 0, 0, 0, 0], Topics, Students)
add_student("Dallas Yan", [2, 0, 1, 2, 0, 1, 1, 0, 0], Topics, Students)
add_student("Wisea Resosudarmo", [3, 2, 2, 1, 0, 0, 0, 0, 0], Topics, Students)
add_student("Xinran Zhu", [3, 2, 1, 0, 1, 0, 0, 0, 0], Topics, Students)
add_student("Angus Ritossa", [4, 0, 2, 0, 1, 0, 0, 0, 0], Topics, Students)
add_student("Tiana Tsang Ung", [2, 2, 2, 1, 0, 0, 0, 0, 0], Topics, Students)
add_student("Fergus Yip", [2, 3, 0, 0, 0, 2, 0, 0, 0], Topics, Students)
add_student("Paula Tennet", [1, 1, 2, 0, 0, 3, 1, 0, 0], Topics, Students)
add_student("Sarthak Sahoo", [3, 2, 0, 0, 2, 0, 0, 0, 0], Topics, Students)
add_student("Yuanyuan Li", [3, 1, 1, 1, 1, 0, 0, 0, 0], Topics, Students)
add_student("Diya Patel", [3, 2, 0, 1, 0, 1, 0, 0, 0], Topics, Students)
add_student("Aksay Ram Moham Valluru", [0, 2, 0, 3, 2, 0, 0, 0, 0], Topics, Students)
add_student("Cece Zhu", [2, 0, 1, 3, 0, 1, 0, 0, 0], Topics, Students)
add_student("Peter Derias", [2, 2, 0, 2, 1, 0, 0, 0, 0], Topics, Students)
add_student("Pengsen Mao", [0, 0, 2, 2, 0, 2, 1, 0, 0], Topics, Students)
add_student("Andrew Xie", [3, 0, 3, 0, 1, 0, 0, 0, 0], Topics, Students)
add_student("Joshua Lam", [3, 0, 0, 1, 0, 3, 0, 0, 0], Topics, Students)
add_student("Shirley Zhou", [0, 3, 0, 0, 2, 1, 1, 0, 0], Topics, Students)
add_student("Sachin Paliwal", [0, 0, 3, 0, 2, 0, 2, 0, 0], Topics, Students)
add_student("Nian Li", [2, 0, 3, 0, 2, 0, 0, 0, 0], Topics, Students)

#Get each student's highest preference
def Membership_Division(Topics_Membership, Student_List):
    Student_Names = list(Student_List.keys())
    Student_Preferences = list(Student_List.values())
    counter_failure = 0
    for i in range(len(Student_Names)):
        max = 0
        highest_topic = "Failure"
        temp_Topics = list(Student_Preferences[i].keys())
        for topic in temp_Topics:
            if Student_Preferences[i][topic] > max:
                max = Student_Preferences[i][topic]
                highest_topic = topic
        if highest_topic == "Failure":
            counter_failure += 1
            continue
        Topics_Membership[highest_topic].update({Student_Names[i]: max})
        Students[Student_Names[i]].update({highest_topic: -1})
        del Student_List[Student_Names[i]]

    if counter_failure == len(Student_Names):
        return False
    return True

No_Team_Students = Students.copy()

def Remove_Lowest(Topic_Members, No_Team_Students):
    Names = list(Topic_Members.keys())
    min = Topic_Members[Names[0]]
    lowest = Names[0]
    for Student in Names:
        if Topic_Members[Student] < min:
            min = Topic_Members[Student]
            lowest = Student
    del Topic_Members[lowest]
    No_Team_Students.update({lowest: Students[lowest]})


Complete = False
while len(No_Team_Students) > 0:
    Remove_Min = True
    result = Membership_Division(Topics_Membership, No_Team_Students)
    if result == False and Complete == True:
        break
    for Topic in list(Topics_Membership.keys()):
        if len(Topics_Membership[Topic]) > Max_Team_Size:
            Remove_Min = False
            Complete = False
            for i in range(len(Topics_Membership[Topic]) - Max_Team_Size):
                Remove_Lowest(Topics_Membership[Topic], No_Team_Students)
    if Remove_Min == True:
        Complete = True
        for Topic in list(Topics_Membership.keys()):
            if len(Topics_Membership[Topic]) < Min_Team_Size:
                for i in range(len(Topics_Membership[Topic])):
                    Remove_Lowest(Topics_Membership[Topic], No_Team_Students)

for topic in Topics:
    print("========================================")
    print(f"{topic}'s Members: ")
    for Student in list(Topics_Membership[topic].keys()):
        print(Student)

print("========================================")
print("Student's Without a Team: ")
for Student in list(No_Team_Students.keys()):
    print(Student)
print("========================================")