import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        answer.config(text=f"Result: {result}")
    except:
        answer.config(text="Invalid calculation")

app = tk.Tk()
app.title("Calculator")
app.geometry("300x200")

tk.Label(app, text="Enter calculation:").pack(pady=10)

entry = tk.Entry(app, width=25)
entry.pack()

tk.Button(app, text="Calculate", command=calculate).pack(pady=15)

answer = tk.Label(app, text="Result:")
answer.pack()

app.mainloop()

