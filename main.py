import tkinter



window = tkinter.Tk()

window.title("My First GUI program")
window.minsize(width=500, height=300)


#Lable

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="bottom")