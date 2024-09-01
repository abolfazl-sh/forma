import abc
from tkinter import *

class Figure(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_
    """

    def __init__(self, color, border_color) -> None:
        self.color = color
        self.border_color = border_color

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def modify(self):
        pass


class Rectangle(Figure):
    def __init__(self, color, border_color) -> None:
        super().__init__(color, border_color)

    def draw(self, width, length, frame):
        canvas = Canvas(frame)
        canvas.create_rectangle(100, 100, 150 + width, 150 + length,
            outline="#fb0", fill="#fb0")
        canvas.pack()

    def modify(self, width, lenght):
        print("figure modified")
        self.draw()


class Squre(Rectangle):
    def __init__(self, color, border_color) -> None:
        super().__init__(color, border_color)

    def draw(self, width, lenght, frame):
        canvas = Canvas(frame)
        canvas.create_rectangle(100, 100, 100 + width, 100 + width,
            outline="#fb0", fill="#fb0")
        canvas.pack()
    def modify(self, wide, lenght):
        print("figure modified")
        self.draw()

class Ovel(Figure):
    def __init__(self, color, border_color) -> None:
        super().__init__(color, border_color)

    def draw(self, width, length, frame):
        canvas = Canvas(frame)
        canvas.create_oval(100, 100, 150 + width, 180,
            outline="#fb0", fill="#fb0")
        canvas.pack()

    def modify(self, width, length):
        pass


class Cyrcle(Ovel):
    def __init__(self, color, border_color) -> None:
        super().__init__(color, border_color)
        
    def draw(self, width, length, frame):
        canvas = Canvas(frame)
        canvas.create_oval(100, 100, 100 + width, 100 + width,
            outline="#fb0", fill="#fb0")
        canvas.pack()

    def modify(self, width, length):
        pass
