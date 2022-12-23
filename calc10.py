import tkinter as tk
import math

# create the main window
root = tk.Tk()

# set the window title and size
root.title("Calculator")
root.geometry("800x600+300+300")

# set the background color to black and orange
root.configure(background='#C8B8DB')

# define a function for each type of calculation
def add():
    # add the "+" operator to the input field
    input_field.set(input_field.get() + "+")
    # set the insertion cursor to the end of the input field
    input_entry.icursor(tk.END)

def subtract():
    # add the "-" operator to the input field
    input_field.set(input_field.get() + "-")
    # set the insertion cursor to the end of the input field
    input_entry.icursor(tk.END)

def multiply(): 
    # add the "*" operator to the input field
    input_field.set(input_field.get() + "*")
    # set the insertion cursor to the end of the input field
    input_entry.icursor(tk.END)

def divide():
    # add the "/" operator to the input field
    input_field.set(input_field.get() + "/")
    # set the insertion cursor to the end of the input field
    input_entry.icursor(tk.END)

def power():
    # add the "**" operator to the input field
    input_field.set(input_field.get() + "**")
    # set the insertion cursor to the end of the input field
    input_entry.icursor(tk.END)

def sin():
    # add the "math.sin()" function to the input field
    input_field.set(input_field.get() + "math.sin()")
    # move the insertion cursor to the middle of the parenthesis
    input_entry.icursor(len(input_field.get()) - 1)

def cos():
    # add the "math.cos()" function to the input field
    input_field.set(input_field.get() + "math.cos()")
    # move the insertion cursor to the middle of the parenthesis
    input_entry.icursor(len(input_field.get()) - 1)

def tan():
    # add the "math.tan()" function to the input field
    input_field.set(input_field.get() + "math.tan()")
    # move the insertion cursor to the middle of the parenthesis
    input_entry.icursor(len(input_field.get()) - 1)

def log():
    # add the "math.log()" function to the input field
    input_field.set(input_field.get() + "math.log()")
    # move the insertion cursor to the middle of the parenthesis
    input_entry.icursor(len(input_field.get()) - 1)

def sqrt():
    # add the "math.sqrt()" function to the input field
    input_field.set(input_field.get() + "math.sqrt()")
    # move the insertion cursor to the middle of the parenthesis
    input_entry.icursor(len(input_field.get()) - 1)

def ln():
    # add the "math.log1p()" function to the input field
    input_field.set(input_field.get() + "math.log1p()")
    # move the insertion cursor to the middle of the parenthesis
    input_entry.icursor(len(input_field.get()) - 1)

def factorial():
    # add the "math.factorial()" function to the input field
    input_field.set(input_field.get() + "math.factorial()")
    # move the insertion cursor to the middle of the parenthesis
    input_entry.icursor(len(input_field.get()) - 1)

def mod():
    # add the "%" operator to the input field
    input_field.set(input_field.get() + "%")
    # set the insertion cursor to the end of the input field
    input_entry.icursor(tk.END)

def pi():
    # add the "math.pi" constant to the input field
    input_field.set(input_field.get() + "math.pi")
    # set the insertion cursor to the end of the input field
    input_entry.icursor(tk.END)

def e():
    # add the "math.e" constant to the input field
    input_field.set(input_field.get() + "math.e")
    # set the insertion cursor to the end of the input field
    input_entry.icursor(tk.END)

# create the input field and set its default value to an empty string
input_field = tk.StringVar()
input_field.set("")

# create a text entry widget for the input field and set its background color to black and orange
input_entry = tk.Entry(root, textvariable=input_field, bg="#F9F4F5", fg="black")

# create a function to calculate the result of the input expression
def calculate(event = 0):
    # try to evaluate the input expression and catch any errors that may occur
    try:
        # evaluate the input expression and store the result in a variable
        result = eval(input_field.get())

        # check if the result is too long to display properly and truncate it if necessary
        if len(str(result)) > 20:
            result = str(result)[:20] + "..."

        #add commas to the result
        formatted_result = format(result, ',')
        # update the input field with the result of the calculation
        input_field.set(formatted_result)
    except:
        # if an error occurs, display the "invalid input" message in the input field
        input_field.set("invalid input")

# bind the "Enter" key to the calculate function
root.bind('<Return>', calculate)

# create a function to clear the input field
def clear():
    input_field.set("")

# Store the button colors in variables
bg_color = "#70587C"
fg_color = "#F9F4F5"

# Create the buttons using the variables
add_button = tk.Button(root, text="+", command=add, bg=bg_color, fg=fg_color)
subtract_button = tk.Button(root, text="-", command=subtract, bg=bg_color, fg=fg_color)
multiply_button = tk.Button(root, text="*", command=multiply, bg=bg_color, fg=fg_color)
divide_button = tk.Button(root, text="/", command=divide, bg=bg_color, fg=fg_color)
power_button = tk.Button(root, text="^", command=power, bg=bg_color, fg=fg_color)
sin_button = tk.Button(root, text="sin", command=sin, bg=bg_color, fg=fg_color)
cos_button = tk.Button(root, text="cos", command=cos, bg=bg_color, fg=fg_color)
tan_button = tk.Button(root, text="tan", command=tan, bg=bg_color, fg=fg_color)
log_button = tk.Button(root, text="log", command=log, bg=bg_color, fg=fg_color)
sqrt_button = tk.Button(root, text="sqrt", command=sqrt, bg=bg_color, fg=fg_color)
ln_button = tk.Button(root, text="ln", command=ln, bg=bg_color, fg=fg_color)
factorial_button = tk.Button(root, text="!", command=factorial, bg=bg_color, fg=fg_color)
mod_button = tk.Button(root, text="%", command=mod, bg=bg_color, fg=fg_color)
pi_button = tk.Button(root, text="π", command=pi, bg=bg_color, fg=fg_color)
e_button = tk.Button(root, text="e", command=e, bg=bg_color, fg=fg_color)
calculate_button = tk.Button(root, text="=", command=calculate, bg=bg_color, fg=fg_color)
clear_button = tk.Button(root, text="clear", command=clear, bg=bg_color, fg=fg_color)


# center the buttons and the input field in the middle of the window
input_entry.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
add_button.place(relx=0.15, rely=0.2, anchor=tk.CENTER)
subtract_button.place(relx=0.25, rely=0.2, anchor=tk.CENTER)
multiply_button.place(relx=0.35, rely=0.2, anchor=tk.CENTER)
divide_button.place(relx=0.45, rely=0.2, anchor=tk.CENTER)
power_button.place(relx=0.55, rely=0.2, anchor=tk.CENTER)
sin_button.place(relx=0.65, rely=0.2, anchor=tk.CENTER)
cos_button.place(relx=0.75, rely=0.2, anchor=tk.CENTER)
tan_button.place(relx=0.85, rely=0.2, anchor=tk.CENTER)
log_button.place(relx=0.15, rely=0.3, anchor=tk.CENTER)
sqrt_button.place(relx=0.25, rely=0.3, anchor=tk.CENTER)
ln_button.place(relx=0.35, rely=0.3, anchor=tk.CENTER)
factorial_button.place(relx=0.45, rely=0.3, anchor=tk.CENTER)
mod_button.place(relx=0.55, rely=0.3, anchor=tk.CENTER)
pi_button.place(relx=0.65, rely=0.3, anchor=tk.CENTER)
e_button.place(relx=0.75, rely=0.3, anchor=tk.CENTER)
calculate_button.place(relx=0.85, rely=0.3, anchor=tk.CENTER)
clear_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# define the button width and height
button_width = 10
button_height = 3

# increase the width and height of the buttons and the input field
add_button.configure(width=button_width, height=button_height)
subtract_button.configure(width=button_width, height=button_height)
multiply_button.configure(width=button_width, height=button_height)
divide_button.configure(width=button_width, height=button_height)
power_button.configure(width=button_width, height=button_height)
sin_button.configure(width=button_width, height=button_height)
cos_button.configure(width=button_width, height=button_height)
tan_button.configure(width=button_width, height=button_height)
log_button.configure(width=button_width, height=button_height)
sqrt_button.configure(width=button_width, height=button_height)
ln_button.configure(width=button_width, height=button_height)
factorial_button.configure(width=button_width, height=button_height)
mod_button.configure(width=button_width, height=button_height)
pi_button.configure(width=button_width, height=button_height)
e_button.configure(width=button_width, height=button_height)
calculate_button.configure(width=button_width, height=button_height)
clear_button.configure(width=button_width, height=button_height)

# define the input field width
input_width = 50

# increase the width of the input field
input_entry.configure(width=input_width)


# run the main event loop
root.mainloop()
