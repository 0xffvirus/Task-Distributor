import math

def askTasks():
    currentTask = 1
    task = input(f"Task {currentTask} (0 to end): ")
    
    tasks = []
    while (task != "0"):
        currentTask += 1
        tasks.append(task)
        task = input(f"Task {currentTask} (0 to end): ")

    team_members = int(input("Enter team members: "))
    maximum_tasks = input("[Optional] Enter maximum tasks per member (leave blank if none): ")

    if maximum_tasks: 
        maximum_tasks = int(maximum_tasks)
    else:
        maximum_tasks = None
    calcTask(tasks, team_members, maximum_tasks)

def calcTask(tasks, team_members, maximum_task_per_member):
    try:
        if (len(tasks) <= 0 or team_members <= 0):
            raise Exception("Invalid input")
        elif maximum_task_per_member:
            required = (math.ceil(len(tasks)/maximum_task_per_member)) 
            if required > team_members:
                raise Exception(f"Not enough team members. team members should be at least {required}\nyou need {required - team_members} more members")
        
        assignments = {}
        for member in range(0,team_members):
            assignments[f"Member {member}"] = []

        currentmember = 0
        for task in tasks:
            assignments[f"Member {currentmember}"].append(task)
            currentmember = ((currentmember + 1) % team_members)

        printTasks(assignments)

    except Exception as e:
        if (str(e) == ("Invalid input")):
            print("========= Invlid Input =========")
            askTasks()
        if (str(e).find("Not enough team members.") >= 0):
            print(e)
            if (input("do you to want change team members? (no to exit): ").lower() == "no"):
                exit()
            else:
                team_members = int(input("Enter team members: "))
                calcTask(tasks, team_members, maximum_task_per_member)


def printTasks(assignments: dict):
    print()
    for member, tasks in assignments.items():
        print(f"{member}: {', '.join(tasks)}")


if __name__=="__main__":
    askTasks()