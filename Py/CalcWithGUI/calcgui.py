import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    root.insert(symbol)
    
def clear_calculation():
    pass

def evaluate_calculation():
    pass

root = tk.Tk()
root.tilte("Calculator")
root.geometry("300x275")
root.resizeable(False, False)
root.configure(bg="darkgray")


root.mainloop()