import tkinter as tk

def calculator():
    try:
        result = eval(entry.get())
        answer.config(text=f"Result: {result}")
    except:
        answer.config(text="Invalid calculation")

app = tk.Tk()
app.title("calculator")
app.geometry("300x200")

tk.Label(app, text="Enter calculation").pack(pady=10)

entry = tk.Entry(app, width=25)
entry.pack()

tk.Button(app, text="Calculate", command=calculator).pack(pady=15)

answer = tk.Label(app, text="Result:")
answer.pack()

app.mainloop()
