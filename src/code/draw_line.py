# Рисование линии
def draw_line(self, p, q, homothety=1.0, color="black"):
    self.canvas.create_line(x(p, homothety), y(p, homothety),
                            x(q, homothety), y(q, homothety),
                            fill=color, width=1)
    self.root.update()