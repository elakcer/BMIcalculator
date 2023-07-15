import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=40,pady=40)

def calculate():
    height = myentry_h.get()
    weight = myentry_w.get()

    if weight == "" or height == "":
        output_label.config(text="Enter both weight and height!")
    else:
        try:
             bmi = float(weight)/((float(height)/100) ** 2)
             output_string = write_output(bmi)
             output_label.config(text=output_string)
        except:
             output_label.config(text="Enter a valid number!")

mylabel_w = tkinter.Label(text="Enter Your Weight(kg)", font=("Arial", 10))
mylabel_w.pack()

myentry_w = tkinter.Entry(width=15)
myentry_w.pack()

mylabel_h = tkinter.Label(text= "Enter Your Height(cm)", font= ("Arial",10))
mylabel_h.pack()

myentry_h= tkinter.Entry(width=15)
myentry_h.pack()

mybutton = tkinter.Button(text="Calculate",command=calculate)
mybutton.pack()

output_label = tkinter.Label()
output_label.pack()

def write_output(bmi):
    output_string = f"your BMİ: {round(bmi,2)}. You are "
    if bmi<=16:
        output_string += "severaly thin!"
    elif 16 < bmi <= 17:
        output_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        output_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        output_string += "normally!"
    elif 25 < bmi <= 30:
        output_string += "overwight!"
    elif 30 < bmi <= 35:
        output_string += "obese class 1!"
    elif 35 < bmi <= 40:
        output_string += "obese class 2"
    elif bmi>40:
        output_string += "obese class 3!"
    return output_string

window.mainloop()