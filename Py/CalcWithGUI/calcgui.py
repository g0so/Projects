import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol) #Append the symbol to the calculation string
    text_result.delete(1.0, "end") # Clear the text widget
    text_result.insert(1.0 , calculation) #Insert the updated calculation into the text widget)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation)) # Evaluate the calculation string
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except (ZeroDivisionError):
        clear_calculation()
        text_result.insert(1.0, "ZeroDivisionError")
    except (SyntaxError): 
        clear_calculation()
        text_result.insert(1.0, "Error")
    except Exception as e:
        clear_calculation()
        text_result.insert(1.0, "Error")
        printf("An unexpected error occurred: ", e)


def clear_calculation():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
#This function clear the text widget

root = tk.Tk() # Create the main window
root.geometry("300x275") #Set the size of the window

text_result = tk.Text(root, height = 2, width = 16, font = ("Times New Roman", 24)) # Create a text widget to display the result
text_result.grid(columnspan = 5)  #Place the text widget in the grid, spanning n columns

btn_1 = tk.Button(root, text = "1", command = lambda: add_to_calculation(1), width = 5, font = ("Times New Roman", 14))
btn_1.grid(row = 2, column = 1) # Create a button for the number 1 and place it at row 2, column 1

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Times New Roman", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Times New Roman", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Times New Roman", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Times New Roman", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Times New Roman", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Times New Roman", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Times New Roman", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Times New Roman", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Times New Roman", 14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text = "+", command=lambda: add_to_calculation("+"), width = 5, font = ("Times New Roman", 14))
btn_plus.grid(row = 2, column = 4)

btn_minus = tk.Button(root, text = "-", command=lambda: add_to_calculation("-"), width = 5, font = ("Times New Roman", 14))
btn_minus.grid(row = 3, column = 4)

btn_multiply = tk.Button(root, text = "*", command=lambda: add_to_calculation("*"), width = 5, font = ("Times New Roman", 14))
btn_multiply.grid(row = 4, column = 4)

btn_divide = tk.Button(root, text = "/", command=lambda: add_to_calculation("/"), width = 5, font = ("Times New Roman", 14))
btn_divide.grid(row = 5, column = 4)

btn_point = tk.Button(root, text = ".", command=lambda: add_to_calculation("."), width = 5, font = ("Times New Roman", 14))
btn_point.grid(row = 5, column = 3)

btn_clear = tk.Button(root, text = "C", command=clear_calculation, width = 5, font = ("Times New Roman", 14))
btn_clear.grid(row = 5, column = 1)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Times New Roman", 14))
btn_equals.grid(row=6, column=4)

btn_left_bracket = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Times New Roman", 14))
btn_left_bracket.grid(row=6, column=1)

btn_right_bracket = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Times New Roman", 14))
btn_right_bracket.grid(row=6, column=2)

root.mainloop() # Start the main event loop, basically the program runs until the window is closed.