import random
import util
import copy

class Graph:
    def __init__(self, v, e, dictIn=None):
        self.V = set(v)
        self.E = set(e)
        if not dictIn:
            self.dict = {v: set() for v in self.V}
            for E in self.E:
                self.dict[E.a].add(E)
                self.dict[E.b].add(E)
        else:
            self.dict = dictIn

    def __repr__(self):
        return "Graph({0}, {1})\n{2}\n\n".format(self.V, self.E, self.dict)

    # Gets a vertex with given index if it exists, else return None.
    def GetVertex(self, i):
        for v in self.V:
            if v.index == i:
                return v
        return None

    # Removes the given vertex v from the graph, as well as the edges attached to it.
    # Removes all isolated vertices from the graph as well.
    def Percolate(self, v):
        edgesToRemove = self.dict[v]
        # print(edgesToRemove)
        # Get attached edges to this vertex, remove them.
        for e in self.dict[v]:
            self.E.remove(e)
        # Remove this vertex.
        self.V.remove(v)
        # Update the dictionary
        for vertex in self.dict:
            self.dict.update({vertex: self.dict[vertex] - edgesToRemove})
        # Remove all isolated vertices.
        to_remove = {u for u in self.V if len(self.dict[u]) == 0}
        # print(to_remove)
        del self.dict[v]
        self.V.difference_update(to_remove)

class PercolationPlayer:
	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == -1
    @staticmethod
    def ChooseVertexToColor(graph, player):
        opgraph = Graph(graph.V, graph.E)
        return [x for x in list(sorted(opgraph.dict, key=lambda x : len(opgraph.dict[x]), reverse=True)) if x.color == -1][0]
        # return random.choice([v for v in graph.V if v.color == -1])


    # `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == player
    @staticmethod
    def ChooseVertexToRemove(graph, player):
        # return random.choice([v for v in graph.V if v.color == player])
        opGraph = Graph(graph.V, graph.E)
        return PercolationPlayer.MinimaxP2(opGraph, 64//len(graph.V), True, player)[1]
    
    @staticmethod
    def MinimaxP2(graph, depth, maximizing, player):
        # Check if the current node is a terminal node
        terminal = PercolationPlayer.IsTerminal(graph, depth, maximizing, player)
        if terminal != None:
            return terminal
        
        # Minimax Algorithm
        if maximizing:
            value = -10e7
            playerValidMoves = [v for v in graph.V if v.color == player]
            bestMove = None
            for moveIndex in range(len(playerValidMoves)):
                tempGraph = Graph(graph.V, graph.E)
                validMoves = sorted([v for v in tempGraph.V if v.color == player], key=lambda x : x.index)
                tempGraph.Percolate(validMoves[moveIndex])
                eval, _ = PercolationPlayer.MinimaxP2(tempGraph, depth - 1, False, player)
                if value < eval:
                    value = eval
                    bestMove = validMoves[moveIndex]
            return value, bestMove
        else:
            value = 10e7
            antiPlayerValidMoves = [v for v in graph.V if v.color != player]
            bestMove = None
            for moveIndex in range(len(antiPlayerValidMoves)):
                tempGraph = Graph(graph.V, graph.E)
                validMoves = sorted([v for v in tempGraph.V if v.color != player], key=lambda x : x.index)
                tempGraph.Percolate(validMoves[moveIndex])
                eval, _ = PercolationPlayer.MinimaxP2(tempGraph, depth - 1, True, player)
                if value > eval:
                    value = eval
                    bestMove = validMoves[moveIndex]
            return value, bestMove
    
    # Checks if the current node is terminal
    # Will return None if not terminal
    # Will return the (value, move) tuple if terminal
    @staticmethod
    def IsTerminal(graph, depth, maximizing, player):
        validMoves = [v for v in graph.V if v.color == player]
        if depth == 0:
            return PercolationPlayer.EvaluationP2(graph, player), None
        
        if len(validMoves) == 0:
            if len(graph.V) == 0:
                return (-10e6, None) if maximizing else (10e6, None)
            else:
                return (-10e6, None)
        
        return None

    @staticmethod
    def EvaluationP2(graph, player):
        playerScore = sum([len(graph.dict[v]) for v in graph.V if v.color == player])
        antiPlayerScore = sum([len(graph.dict[v]) for v in graph.V if v.color != player])
        return playerScore - antiPlayerScore
        # return len([v for v in graph.V if v.color == player]) - len([v for v in graph.V if v.color != player])

# Feel free to put any personal driver code here.
def main():
    pass

if __name__ == "__main__":
    main()