from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)
window.config(padx=50,pady=40)

weight_label = Label(text="Enter Your Weight (kg)",font='Helvetica 10 bold')
weight_label.config(fg="black")
weight_label.pack(pady=5)

weight_entry = Entry()
weight_entry.config(width=20)
weight_entry.pack(pady=5)

height_label = Label(text="Enter Your Height (cm)",font='Helvetica 10 bold')
height_label.config(fg="black")
height_label.pack(pady=5)

height_entry = Entry()
height_entry.config(width=20)
height_entry.pack(pady=10)

result_label = Label(text="",font='Helvetica 10 normal')

def calculate_and_categorize_bmi(weight_value,height_value):
    bmi = weight_value / pow(height_value / 100, 2)

    if bmi < 18.5:
        category = "You are under weight."
    elif 18.5 <= bmi < 25:
        category = "You are normal weight."
    elif 25 <= bmi < 30:
        category = "You are over weight."
    elif 30 <= bmi < 35:
        category = "You are obesity (class 1)."
    elif 35 <= bmi < 40:
        category = "You are obesity (class 2)."
    else:
        category = "You are extreme obesity."

    result_label.config(text=f"Your BMI is {bmi:.2f}. {category}",fg="black")

def check_entries():
    weight_value = weight_entry.get().strip()
    height_value = height_entry.get().strip()

    if weight_value == "" or height_value == "":
        result_label.config(text="Enter both weight and height!", fg="red")
        return

    try:
        weight_value = float(weight_value)
        height_value = float(height_value)

        if weight_value > 0 and height_value > 0:
            calculate_and_categorize_bmi(weight_value,height_value)
        else:
            result_label.config(text="Please enter positive values!",fg="red")

    except ValueError:
        result_label.config(text="Please enter numbers only!", fg="red")

calculate_button = Button(text="Calculate",width=10,command=check_entries)
calculate_button.pack()
result_label.pack()

window.mainloop()