classes = []

def main():
    try:
        f = open("class_list.txt", 'r')
        lines = f.readlines()
        if len(lines) == 0:
            print("Welcome first time user!")
            f.close()
            makenewclass()
            
        else:
            for line in lines:
                classes.append(line.strip())
            f.close()
    except:
        print("Welcome first time user!")
        makenewclass()
    
    
    #mainloop begin
    while True:
        print("*"*40)
        print(" ")
        print("Options:")
        print("Quit")
        print("show grades")
        print("add class")
        print("manage class")
        print("^^^^ With manage class, you can add grades, or get more")
        print("     specific info about your grade in that class")
        print(" ")
        print("*"*40)

        while True:
            choice = input("Quit, show grades, add class, or manage class").upper()
            if choice == "SHOW GRADES" or choice == "ADD CLASS" or choice == "MANAGE CLASS" or choice == "QUIT":
                break
        if choice == "QUIT":
            break
        if choice == "SHOW GRADES":
            print(" ")
            print("*"*40)
            print("Here are your current grades:\n")
            for course in classes:
                grade = calculate_grade(course)
                print(course + ": " + str(grade))


        if choice == "ADD CLASS":
            makenewclass()




            
        if choice == "MANAGE CLASS":
            print(" ")
            print("*"*40)
            print(" ")
            
            for course in classes:
                print(course)
            inp = input("Which course would you like to manage (no spaces)?\n").upper()
            chosen = 0
            
            while True:
                if inp in classes:
                    chosen = inp
                    break
                else:
                    print("Oops, you did something wrong.")
                    inp = input("Which course would you like to manage (no spaces)?\n").upper()

            while True:
                print("Your choices for " + chosen + ":")
                print("QUIT")
                print("ADD GRADE")
                print("GET INFO")
                print("^^^ This will get more specific info about your grade")
                print(" ")
                inp = input("Which option would you like").upper().strip()
                
                if inp == "QUIT":
                    break
                
                if inp == "ADD GRADE":
                    already_done = []
                    i = 1
                    f = open(chosen + ".txt", "r")
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip()
                    f.close()
                    while True:
                        if lines[i] == "NONE\n":
                            break
                        category = lines[i]
                        i = i + 2
                        already_done.append(category.strip())
                    categ = 0
                    while True:
                        print(" ")
                        for category in already_done:
                            print(category)
                        categ = input("Which category would you like\n").upper()
                        if categ in already_done:
                            break

                    f = open(chosen + ".txt", "a")
                    f.write(categ + "\n")

                    while True:
                        try:
                            num = float(input("Input grade (number):"))
                            break
                        except:
                            pass

                    f.write(str(num)+"\n")
                    f.close()


 
                    
                if inp == "GET INFO":
                    print("Your grade in " + chosen + ": " + str(calculate_grade(chosen)))
                    f = open(chosen + ".txt", "r")
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip()
                    i = 1
                    categories = []
                    percentages = []
                    
                    while True: #put every category into categories
                        if lines[i] == "NONE\n":
                            break
                        else:
                            categories.append(lines[i])
                            percentages.append(float(lines[i+1]))
                            i = i + 2
                            
                    for x in range(0, len(categories)):
                        print(categories[x] + " (" + str(percentages[x]) + "%):")
                        j = i+1
                        grades = []
                        while True:
                            try:
                                if lines[j] == categories[x]:
                                    grades.append(float(lines[j+1]))
                                j = j+2
                            except:
                                break
                        for grade in grades:
                            print(str(grade))
                        if len(grades) > 0:
                            average = sum(grades)/len(grades)
                            print("Category average: " + str(average))
                        else:
                            print("No grades in this category")
                        print(" ")
                                    
                        


def calculate_grade(course):
    f = open(course + ".txt", "r")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
    i = 1
    categories = []
    percentages = []
    
    while True: #put every category into categories
        if lines[i] == "NONE\n":
            break
        else:
            categories.append(lines[i])
            percentages.append(float(lines[i+1]))
            i = i + 2

    averages = []
    percentages_new = []
    for x in range(0, len(categories)):
        j = i+1
        grades = []
        while True:
            try:
                if lines[j] == categories[x]:
                    grades.append(float(lines[j+1]))
                j = j+2
            except:
                break
        if len(grades) > 0:
            average = sum(grades)/len(grades)
            averages.append(average)
            percentages_new.append(percentages[x])

    total_grade = 0
    total_possible = sum(percentages_new)
    for y in range(0, len(percentages_new)):
        total_grade = total_grade + (percentages_new[y]*averages[y])/100
    if total_possible == 0:
        return 0
    return((total_grade/total_possible)*100)

    f.close()





def makenewclass():
    print("welcome to making a new class!")
    print("*"*40)

    while True:
        department = input("Input department abbreviation e.g. COMP   :\n")
        course = input("\nWhat number is the course? e.g. 101      :\n")
        try:
            x = int(course)
            break
        except:
            print("oops, be sure to type an integer for the course number!")

    course_name = department.strip().upper() + str(course)
    if course_name in classes:
        print("Class already exists")
        return
    classes.append(course_name)
    
    f = open("class_list.txt", 'a')
    f.write(course_name+"\n");
    f.close()
    
    f = open(course_name + ".txt", "a")
    f.write(course_name+"\n")

    
    total = 0
    while True:
        category = input("Please input a grading category e.g. 'Homework'\n")

        while True:
            num = input("What percent is this category?\n")
            try:
                num = float(num)
                if num < 0.5:
                    print("I'm assuming you meant to type " + str(num*100))
                    num = num * 100
                break
            except:
                print("Not a number.....")
                pass
        
        f.write(category.upper() + "\n")
        f.write(str(num) + "\n")

        total += num
        if total >= 100:
            break

    f.write("NONE\n")    

    f.close()













    

main()
