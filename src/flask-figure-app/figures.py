
class Figure():
    def __init__(self, color="#808080"):
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

class Square(Figure):
    pass

class Circle(Figure):
    pass

class Triangle(Figure):
    pass

class FigureService:
    def __init__(self):
        self.figures = {
            "square": Square(),
            "circle": Circle(),
            "triangle": Triangle()
        }

    def change_color(self, figure_type, new_color):
        if figure_type in self.figures:
            self.figures[figure_type].change_color(new_color)
            return True
        return False

    def change_color_all(self, new_color):
        for figure in self.figures.values():
            figure.change_color(new_color)

    def get_colors(self):
        return {figure_type: figure.color for figure_type, figure in self.figures.items()}