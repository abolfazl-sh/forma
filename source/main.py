from tkinter import *
from tkinter import ttk
from figures import *


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x500')
        self.master.title("Figure")
        self.main()
        self.rectangle = Rectangle(1, 1)
        self.squre = Squre(1, 1)
        self.ovel = Ovel(1, 1)
        self.cyrcle = Cyrcle(1, 1)

        self.figures = {"Rectangle": self.rectangle, "Squre": self.squre,
                        "Ovel": self.ovel, "Cyrcle": self.cyrcle}

    def main(self):

        for i in self.master.winfo_children():
            i.destroy()
        self.main_fram = Frame(self.master, width=500, height=500)
        self.main_fram.pack()

        title_lbl = Label(self.main_fram, text="Draw Figure",
                          width=20, font=("bold", 20))
        title_lbl.place(x=90, y=53)
        title_lbl.pack()

        figure_lbl = Label(self.main_fram, text="Figure Type",
                           width=20, font=("bold", 10))
        figure_lbl.place(x=80, y=130)
        figure_lbl.pack()

        figure_cbox = ttk.Combobox(
            self.main_fram, state='readonly', values=['Rectangle', 'Squre', 'Ovel', 'Cyrcle'])
        figure_cbox.place(x=240, y=130)
        figure_cbox.current(0)
        figure_cbox.pack()

        draw_btn = Button(self.main_fram, text='Draw', width=20,
                          bg='black', fg='black', command=lambda: self.figure(figure_cbox.get()))
        draw_btn.place(x=180, y=180)
        draw_btn.pack()

    def figure(self, fig):
        for i in self.master.winfo_children():
            i.destroy()
        self.figure_fram = Frame(self.master, width=500, height=500)
        self.figure_fram.pack()

        title_lbl = Label(self.figure_fram, text=fig,
                          width=20, font=("bold", 20))
        title_lbl.place(x=90, y=53)
        title_lbl.pack()

        self.figures.get(fig).draw(100, 100, self.figure_fram)

        draw_btn = Button(self.figure_fram, text='back', width=20,
                          bg='black', fg='black', command=self.main)
        draw_btn.place(x=80, y=580)
        draw_btn.pack()


root = Tk()
app(root)
root.mainloop()
