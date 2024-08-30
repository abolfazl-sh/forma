import abc


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

    def draw(self):
        print("figure drawed")

    def modify(self):
        print("figure modified")
        self.draw()


class Squre(Rectangle):
    def __init__(self, color, border_color) -> None:
        super().__init__(color, border_color)


class Ovel(Figure):
    def __init__(self, color, border_color) -> None:
        super().__init__(color, border_color)

    def draw():
        pass

    def modify():
        pass


class Cyrcle(Ovel):
    def __init__(self, color, border_color) -> None:
        super().__init__(color, border_color)
