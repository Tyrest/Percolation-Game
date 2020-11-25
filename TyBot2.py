import random
import util
import copy

class Graph:
    def __init__(self, vDict):
        # self.dict = copy.deepcopy(vDict)
        self.dict = {k:set(v) for k,v in vDict.items()}

    def __repr__(self):
        return "Graph({0})".format(self.dict)

    # Removes the given vertex v from the graph, as well as the edges attached to it.
    # Removes all isolated vertices from the graph as well.
    def Percolate(self, v):
        # Delete the dictionary key
        del self.dict[v]
        #Delete all versions of the vertex from the dictionary
        for vertex in self.dict:
            self.dict[vertex].discard(v)
        # Remove all isolated vertices.
        to_remove = {u for u in self.dict if len(self.dict[u]) == 0}
        for isoVertex in to_remove:
            del self.dict[isoVertex]

class PercolationPlayer:
	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == -1
    @staticmethod
    def ChooseVertexToColor(graph, player):
        # return random.choice([v for v in graph.V if v.color == -1])
        opgraph = Graph(PercolationPlayer.SetsToDict(graph))
        uncoloredVertices = [v for v in opgraph.dict if v.color == -1]
        move = uncoloredVertices[0]
        value = -10e4
        for v in uncoloredVertices:
            aPV = [x for x in opgraph.dict[v] if v.color == player]
            aEV = [x for x in opgraph.dict[v] if v.color == 1 - player]
            hValue = PercolationPlayer.VertexHeuristic(v, opgraph, player, aPV, aEV)
            if hValue > value:
                move = v
                value = hValue
        return move

    @staticmethod
    def VertexHeuristic(x, graph, player, aPV, aEV):
        # Degree of the vertex
        score = len(graph.dict[x])
        return score

    # `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == player
    @staticmethod
    def ChooseVertexToRemove(graph, player):
        # return random.choice([v for v in graph.V if v.color == player])
        opGraph = Graph(PercolationPlayer.SetsToDict(graph))
        depth = 64//len(graph.V)
        if len(graph.V) < 12:
            depth = 12
        value, move = PercolationPlayer.MinimaxP2(opGraph, depth, True, player)
        return move

    @staticmethod
    def SetsToDict(graph):
        vDict = {v: set() for v in graph.V}
        for e in graph.E:
            vDict[e.a].add(e.b)
            vDict[e.b].add(e.a)
        return vDict
    
    @staticmethod
    def MinimaxP2(graph, depth, maximizing, player):
        # print("depth: {0}\n{1}".format(depth, graph))
        # Check if the current node is a terminal node
        terminal = PercolationPlayer.IsTerminal(graph, depth, maximizing, player)
        if terminal != None:
            return terminal

        # Minimax Algorithm
        if maximizing:
            value = -10e7
            playerValidMoves = [v for v in graph.dict if v.color == player]
            bestMove = None
            for moveIndex in range(len(playerValidMoves)):
                tempGraph = Graph(graph.dict)
                validMoves = sorted([v for v in tempGraph.dict if v.color == player], key=lambda x : x.index)
                tempGraph.Percolate(validMoves[moveIndex])
                eval, _ = PercolationPlayer.MinimaxP2(tempGraph, depth - 1, False, player)
                if value < eval:
                    value = eval
                    bestMove = validMoves[moveIndex]
            return value, bestMove
        else:
            value = 10e7
            antiPlayerValidMoves = [v for v in graph.dict if v.color != player]
            bestMove = None
            for moveIndex in range(len(antiPlayerValidMoves)):
                tempGraph = Graph(graph.dict)
                validMoves = sorted([v for v in tempGraph.dict if v.color != player], key=lambda x : x.index)
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
        if depth == 0:
            return PercolationPlayer.EvaluationP2(graph, player), None
        elif len(graph.dict) == 0:
            return (-10e6, None) if maximizing else (10e6, None)
        elif len([v for v in graph.dict if v.color == player]) == 0:
            return (-10e6, None)
        elif len([v for v in graph.dict if v.color != player]) == 0:
            return (10e6, next(iter(graph.dict)))
        
        return None

    @staticmethod
    def EvaluationP2(graph, player):
        # playerScore = len([v for v in graph.dict if v.color == player])
        playerScore = sum([len(graph.dict[v]) for v in graph.dict if v.color == player]) -\
                      2 * len([v for v in graph.dict if v.color == player])
        antiPlayerScore = sum([len(graph.dict[v]) for v in graph.dict if v.color != player]) -\
                          2 * len([v for v in graph.dict if v.color != player])
        return playerScore - antiPlayerScore

# Feel free to put any personal driver code here.
def main():
    pass

if __name__ == "__main__":
    main()