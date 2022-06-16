import tkinter as tk

root = tk.Tk()

root.title("SE226_Lab_10")

root.geometry("650x650")

def read():
    textBox.delete("1.0", tk.END)
    file = open('Marvel.txt')
    read_text = file.read()
    textBox.insert("end", read_text)


def calculate():
    textBox.delete("1.0", tk.END)
    file = open('Marvel.txt')
    read_text = file.read()
    read_list = []
    for i in read_text.split():
        read_list.append(i)

    for i in read_list:
        string = str("The frequency of '" + str(i) + "' is -> " + str(read_list.count(i)) + "\n")
        textBox.insert(tk.INSERT, string)

    frame.pack(expand=True)


label1 = tk.Label(root, text="To read the from the file press READ\n"
                             "To calculate the frequency of the words in file press CALCULATE\n"
                             "To exit the program press EXIT")
label1.pack()

frame = tk.LabelFrame(root, text="-Text Screen-")
frame.pack()

textBox = tk.Text(frame)
textBox.pack()

button1 = tk.Button(text="READ", bg="white", fg="black", font="Notomono 18", command=read)
button1.place(x=125, y=560)

button2 = tk.Button(text="CALCULATE", bg="white", fg="black", font="Notomono 18", command=calculate)
button2.place(x=240, y=560)

button3 = tk.Button(text="EXIT", bg="white", fg="black", font="Notomono 18", command=exit)
button3.place(x=425, y=560)

root.mainloop()
