# Площадь грани
def area(self):
    # площадь треугольника, построенного на двух векторах
    def __triangle_area(edge_1, edge_2):
        return edge_1.cross(edge_2).magnitude() / 2
    area = 0.0
    # грань может иметь любое число вершин
    for i in range(1, len(self.vertexes) - 1):
        edge_1 = self.vertexes[0] - self.vertexes[i]
        edge_2 = self.vertexes[i+1] - self.vertexes[i]
        area +=  __triangle_area(edge_1, edge_2)
    return area