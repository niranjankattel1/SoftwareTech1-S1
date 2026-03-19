from tkinter import *
import tkinter as tk

class MyApp:

    def __init__(self, root):

        root.title("My app")
        root.geometry("500x400")
        root.maxsize(1000,800)

        frame = Frame(root, width=500, height=400, borderwidth=2, relief="sunken")
        frame.grid(row=0, column=0)



        self.label_text = StringVar(value="Some label text")
        label = Label(frame, textvariable=self.label_text)
        label.grid(column=0, row=0)
        # label.grid(column=2, row=3)
    #     # label.pack()
    #     # label.pack(side=tk.LEFT)

        # label["text"] = "New label text"
        # label["font"] = ("Courier", 40)

        label.configure(text="New label text", font=("Poppins", 40))

        self.entry_text = StringVar(value="")
        entry = Entry(frame, textvariable=self.entry_text)
        entry.grid(column=0, row=1)

        label = Label(frame, textvariable=self.entry_text)
        label.grid(column=0, row=2)
    #     # entry.pack(side=tk.LEFT)
    #     # entry.place(x=100, y=50)
    #     # entry.grid(column=3, row=1)

    #     # label["textvariable"] = entry_text

        button = Button(root, text="Clear", command=self.press_button)
    #     # button.place(x=0, y=0)
    #     # button.configure(width=10, height=2)
    #     # button.configure(width=10, height=5, font=("Courier", 40))
    #     # button.pack(side=tk.LEFT)
        button.grid(column=0, row=3, sticky=(W))

    #     self.list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
    #     list_items = StringVar(value=self.list_item_strings)
    #     listbox = Listbox(root, listvariable=list_items)
    #     # listbox.pack(side=tk.LEFT, padx=40, pady=20)
    #     listbox["height"] = 3
    #     listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
    #     # listbox.grid(column=2, row=2)


    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)


    # def select_item(self, index):
    #     selected_item = self.list_item_strings[index[0]]
    #     print(selected_item)


root = Tk()
MyApp(root)
root.mainloop()
