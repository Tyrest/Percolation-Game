# Percolation Game Bot
- Implements minimax algorithm to achieve around a 85% winrate against random bot
- Implements custom graph class to speed up minimax tree search
- Simple evaluation method (number of nodes for each color left in graph)

# Percolation Game Created by Mr. Redmond
Stichard and Tichael Play a Percolation Game
Stichard Reinberg and Tichael Mhibodeaux are best friends who decide one day that they'd like to play a game on the BRG Gp(2K) - a BRG with an even number of vertices. The game proceeds in two phases: phase 1 is the "coloring" phase, and phase 2 is the "removal" phase.

In phase 1, Stichard and Tichael take turns coloring each of the 2K vertices of the graph either Silver or Teal - Stichard uses Silver, Tichael prefers Teal. Stichard gets to color first.

Then, in phase 2 of the game, they remove vertices from the graph, with Stichard playing first again. On a player's turn, they are allowed to remove any vertex of the graph that is colored their color. Removing a graph vertex in this way also deletes all of the edges attached to that vertex. If this removal leaves a vertex with no edges attached to it (an "isolated" vertex), that isolated vertex is also removed. If the graph starts out with isolated vertices, the first player to move gets to remove those vertices upon completion of their move. A player loses when there are no vertices of their color left to remove.
