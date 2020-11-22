# d1 = {x:{y for y in range(x)} for x in range(5)}
# print(d1)
# d1[1].discard(0)
# print(d1)
# v = 0
# for vertex in d1:
#     d1[vertex].discard(v)
# print(d1)
# to_remove = {u for u in d1 if len(d1[u]) == 0}
# print(to_remove)
# for isoVertex in to_remove:
#     del d1[isoVertex]
# print(d1)
# print([v for v in d1])
# print(list(d1))

import TyBot2
import util

graph = util.BinomialRandomGraph(2, 1)
opgraph = TyBot2.Graph(TyBot2.PercolationPlayer.SetsToDict(graph))
print(opgraph)
opgraph.Percolate(sorted([v for v in opgraph.dict if v.color != 1], key=lambda x : x.index)[0])
print(opgraph)
if len([v for v in opgraph.dict if v.color == 1]) == 0:
    if len(opgraph.dict) == 0:
        print(1)
    else:
        print(0)