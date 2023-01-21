from tkinter import *


window = Tk()
window.title("BENİM İLK DENEMEM")
window.minsize(width=600, height=300)


def clicked():
    miles_deger = float(entry.get())
    deger = miles_deger * 1.609
    my_label3.config(text=f"{deger}")


# Label1 sol
my_label = Label(text="I am a labe", font=("Arial", 24, "bold"))
my_label.config(text="is equal to")
my_label.grid(column=1, row=2)
my_label.config(padx=50, pady=50)

# Label2 sag
my_label2 = Label(text="Km", font=("Arial", 24, "bold"))
my_label2.config(text="Km")
my_label2.grid(column=3, row=2)

# Enrty
entry = Entry(width=10)
entry.grid(column=2, row=1)

# Label3 orta
my_label3 = Label(text="0", font=("Arial", 24, "bold"))
# my_label3.config(text="0\t")
my_label3.grid(column=2, row=2)

# Label4 üst sag
my_label4 = Label(text="Miles", font=("Arial", 24, "bold"))
my_label4.config(text="Miles")
my_label4.grid(column=3, row=1)

# Button
button = Button(width=10, command=clicked)
button.config(text="Calculate")
button.grid(column=2, row=3)



window.mainloop()
