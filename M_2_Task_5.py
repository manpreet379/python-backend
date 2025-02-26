import csv

class Student:
   
    students = [] 
    def __init__(self, student_id, name, age, grade):
      
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        Student.students.append(self)



    def validate_record(student_id, name, age, grade):
        for student in Student.students:
            if student.student_id==student_id:
                return False
        return True
    
    def get_age(self):
       
        return self.age

    def set_age(self, age):
       
        self.age = age

    def get_grade(self):
       
        return self.grade

    def set_grade(self, grade):
       
        self.grade = grade


    @classmethod
    def save_to_csv(cls, filename="students.csv"):
        """Saves all student records to the CSV file."""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Grade"]) 
            for student in cls.students:
                writer.writerow([student.student_id, student.name, student.age, student.grade])

    @classmethod
    def read_from_csv(cls, filename="students.csv"):
        """Reads and displays the contents of the CSV file."""
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    @classmethod
    def add_record(cls, student_id, name, age, grade, filename="students.csv"):
        if not cls.validate_record(student_id, name, age, grade):
            print("Record already exists")
            return
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, age, grade])
        cls(student_id, name, age, grade)

    @classmethod
    def modify_record(cls, student_id, new_name, new_age, new_grade, filename="students.csv"):
       
        rows = []
        modified = False
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)

            for i, row in enumerate(rows):
                if row and row[0] == str(student_id):
                    rows[i] = [str(student_id), new_name, str(new_age), new_grade]
                    modified = True
                    break

            if modified:
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                print(f"Record with ID {student_id} modified.")
                for student in cls.students:
                    if student.student_id == student_id:
                        student.name = new_name
                        student.age = new_age
                        student.grade = new_grade
                        break
            else:
                print(f"Record with ID {student_id} not found.")

        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    @classmethod
    def delete_record(cls, student_id, filename="students.csv"):
       
        rows = []
        deleted = False
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)

            new_rows = [rows[0]]  # Keep header row
            for row in rows[1:]:
                if row and row[0] != str(student_id):
                    new_rows.append(row)
                else:
                    deleted = True

            if deleted:
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(new_rows)
                print(f"Record with ID {student_id} deleted.")
                for student in cls.students[:]:
                    if student.student_id == student_id:
                        cls.students.remove(student)
                        break
            else:
                print(f"Record with ID {student_id} not found.")

        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    @classmethod
    def search_record(cls, student_id, filename="students.csv"):
       
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == str(student_id):
                        print("Record Found:", row)
                        return
                print(f"Record with ID {student_id} not found.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")




student1 = Student(1, "Abhishek", 20, "A")
student2 = Student(2, "Varun", 21, "B")


Student.save_to_csv()
Student.read_from_csv()

student1.set_age(22)
student2.set_grade("A+")
Student.save_to_csv()

Student.add_record(3, "Manpreet", 19, "A+")
Student.read_from_csv()

Student.modify_record(2, "Rohan", 22, "A")
Student.read_from_csv()

Student.delete_record(3)
Student.read_from_csv()

Student.search_record(1)
Student.search_record(3)
Student.add_record(2, "Varun", 21, "B")