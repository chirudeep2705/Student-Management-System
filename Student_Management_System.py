import tkinter as tk

def delete_student():
    selected = student_listbox.curselection()
    if selected:
        student_listbox.delete(selected)
        message_entry.config(text="Student deleted successfully", fg="green")
    else:
        message_entry.config(text="Select a student to delete", fg="red")

def add_student():
    name = name_student.get()
    age = age_student.get()
    course = course_var.get()
    gender = gender_var.get()

    if name == "" or age == "" or course == "Select Course" or gender == "":
        message_entry.config(text="Please fill all fields", fg="red")
        

    if not age.isdigit():
        message_entry.config(text="Age must be a number", fg="red")
        return

    student_data = f"Name: {name} | Age: {age} | Course: {course} | Gender: {gender}"
    student_listbox.insert(tk.END, student_data)

    name_student.delete(0, tk.END)
    age_student.delete(0, tk.END)
    course_var.set("Select Course")
    gender_var.set("")

obj = tk.Tk()
obj.title("Student Management System")
obj.geometry("700x600")

title_label = tk.Label(obj, text="Student Management System",font=("bold"))
title_label.pack(pady=10)

frame = tk.Frame(obj)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_student = tk.Entry(frame)
name_student.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Age").grid(row=1, column=0, padx=10, pady=5)
age_student= tk.Entry(frame)
age_student.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Course").grid(row=2, column=0, padx=10, pady=5)
course_var = tk.StringVar()
course_var.set("Select Course")
course_menu = tk.OptionMenu(frame, course_var, "IT", "CSE", "ECE", "MECH", "CIVIL")
course_menu.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Gender").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
male_gender = tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male")
female_gender = tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female")
male_gender.grid(row=3, column=1, sticky="w")
female_gender.grid(row=3, column=1, padx=70, sticky="w")

add_student = tk.Button(obj, text="Add Student", command=add_student)
add_student.pack(pady=10)

message_entry = tk.Label(obj, text="", font=("Arial", 10))
message_entry.pack()

student_listbox = tk.Listbox(obj, width=600, height=16)
student_listbox.pack(pady=10)

delete_entry = tk.Button(obj, text="Delete Selected", command=delete_student)
delete_entry.pack(pady=10)

obj.mainloop()
