import tkinter as tk

# I am creating an application with tkinter that calculates body mass index/BMI


window = tk.Tk()
window.geometry("300x200")

height_label = tk.Label(text="height")
height_label.grid(column=0, row=1)

weight_label = tk.Label(text="weight")
weight_label.grid(column=0, row=2)

height = tk.Entry(master=window)
height.grid(column=1, row=1)

weight = tk.Entry(master=window)
weight.grid(column=1, row=2)

text_answer = tk.Text(master=window, height=10, width=20)
text_answer.grid(column=1, row=5)


def run_calculation():
    height_float = float(height.get())
    weight_float = float(weight.get())
    body_mass = (weight_float / (height_float * height_float))
    print('Your body mass index is ', body_mass)
    if body_mass <= 18.5:
        print('you are underweight')
    if body_mass <= 24.9:
        print('You are normal weight')
    if body_mass >= 30:
        print('sorry, But you are overweight')
    text_answer.insert('1.0', body_mass)


button = tk.Button(text="Calculate BMI", command=run_calculation)
button.grid(column=1, row=4)

window.mainloop()













