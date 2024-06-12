# вспомогательный массив
buf = line.split()
# количество вершин очередной грани
size = int(buf.pop(0))
# кол-во хороших точек в грани
good_points_num = 0
# массив вершин этой грани
vertexes = []
for n in buf:
    if self.vertexes[int(n) - 1].is_good:
        good_points_num += 1
    vertexes.append(self.vertexes[int(n) - 1])
# задание рёбер грани
for n in range(size):
    self.edges.append(Edge(vertexes[n - 1], vertexes[n]))
# задание самой грани
self.facets.append(Facet(vertexes))
if good_points_num == 1:
    orig_vertexes = [_vertexes[int(n) - 1] for n in buf]
    self.good_area += Facet(orig_vertexes).area()