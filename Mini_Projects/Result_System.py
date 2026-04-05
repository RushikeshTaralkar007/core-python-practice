##################################     MINI PROJECT 4 (Week 4)      ###################################

################################  Student Management + Result System   ##################################
#######################   Used Python : File Handling & Exception Handling   ############################

################################## MINI PROJECT 4 (Week 4) ##################################

File_Name = r"C:\Desktop\Python\Git_Core_Python\core-python-practice\students.txt"


def calculate_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 35:
        return "C"
    else:
        return "Fail"



# load Data

def load_data():
    students = []
    try:
        with open(File_Name, "r") as file:
            next(file)

            for line in file:
                data = line.strip().split(",")

                if len(data) < 12:
                    continue

                student = {
                    "id": data[0],
                    "roll": data[1],
                    "name": data[2],
                    "course": data[3],
                    "dept": data[4],
                    "age": int(data[5]),
                    "attendance": int(data[6]),   
                    "marks": list(map(int, data[7:12]))
                }

                students.append(student)

    except FileNotFoundError:
        print("File Not Found!")
    except Exception as e:
        print("Error:", e)

    return students


# Result Analysis

def show_result(students):
    print("\n Student Results")
    print("=" * 60)

    for s in students:
        total = sum(s["marks"])
        percentage = total / 5
        grade = calculate_grade(percentage)

        print(f"{s['roll']} | {s['name']} | {percentage:.2f}% | Grade: {grade}")


# Toppers 

def show_toppers(students):
    print("\n Top 5 Students")

    ranked = []

    for s in students:
        percentage = sum(s['marks']) / 5
        ranked.append((percentage, s))

    ranked.sort(key=lambda x: x[0], reverse=True)

    for i in range(min(5, len(ranked))):
        p, s = ranked[i]
        print(f"{i+1}. {s['name']} ({s['roll']}) - {p:.2f}%")



# Search Student 

def search_student(students):
    roll = input("Enter Roll_No: ")

    found = False

    for s in students:
        if s['roll'] == roll:
            total = sum(s['marks'])
            percentage = total / 5
            grade = calculate_grade(percentage) 

            print("\n Student Found")
            print("-" * 40)
            print(f"Name: {s['name']}")
            print(f"Course: {s['course']}")
            print(f"Department: {s['dept']}")
            print(f"Attendance: {s['attendance']}%")
            print(f"Percentage: {percentage:.2f}%")
            print(f"Grade: {grade}")

            found = True
            break

    if not found:
        print(" Student Not Found")



# Attendance Warnning 

def attendance_warning(students):
    print("\n Low Attendance Students (<75%)")

    found = False

    for s in students:
        if s['attendance'] < 75:
            print(f"{s['name']} ({s['roll']}) - {s['attendance']}%")
            found = True

    if not found:
        print(" All students have good attendance")


# Failed Student 

def fail_student(students):
    print("\n Failed Students")

    found = False

    for s in students:
        if any(m < 35 for m in s['marks']):
            print(f"{s['name']} ({s['roll']}) - Marks: {s['marks']}")
            found = True

    if not found:
        print(" No failed students")

## Export i txt file 

def export_pretty_txt(students):
    try:
        with open("students_pretty.txt", "w") as f:

            # Proper header with spacing
            f.write(f"{'ID':<5} {'RollNo':<8} {'Name':<20} {'Course':<25} {'Dept':<15} {'Age':<5} {'Att%':<6} {'Total':<8} {'Per%':<8} {'Grade':<6}\n")
            f.write("-" * 120 + "\n")

            for s in students:
                total = sum(s["marks"])
                per = total / 5
                grade = calculate_grade(per)

                f.write(
                    f"{s['id']:<5} {s['roll']:<8} {s['name']:<20} {s['course']:<25} "
                    f"{s['dept']:<15} {s['age']:<5} {s['attendance']:<6} "
                    f"{total:<8} {per:<8.2f} {grade:<6}\n"
                )

        print("TXT File Created")

    except Exception as e:
        print(" Error:", e)


# Main Menu 

def main():
    students = load_data()

    if not students:
        return

    while True:
        print("\n" + "=" * 50)
        print(" Student Analytics System")
        print("=" * 50)

        print("1. Show All Results")
        print("2. Show Top 5 Students")
        print("3. Search Students")
        print("4. Low Attendance Report")
        print("5. Failed Students")
        print("6. Exit")
        print("7. Export In TxT File")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                show_result(students)
            elif choice == 2:
                show_toppers(students)
            elif choice == 3:
                search_student(students)
            elif choice == 4:
                attendance_warning(students)
            elif choice == 5:
                fail_student(students)
            elif choice == 6:
                print(" Exiting...")
                break
            elif choice == 7:
                export_pretty_txt(students)
                
            else:
                print(" Invalid choice")
            

        except ValueError:
            print(" Enter a valid number")
        except Exception as e:
            print(" Error:", e)

main()