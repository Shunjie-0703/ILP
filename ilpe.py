import networkx as nx
import matplotlib as plt
import matplotlib.pyplot as mlp
import pandas as pd
# fh = open("ilplist.txt","rb")
# file = 'ilplist.txt'
#F = nx.read_edgelist("ilplist.txt", create_using = nx.DiGraph(), nodetype=int)
from networkx import Graph

g = nx.DiGraph ()
g.add_node (1, po=(10,8))
g.add_node(2,  po=(20,8))
g.add_node(3,  po=(15,6))
g.add_node(4,  po=(15,5))
g.add_node(5,  po=(17,3))
g.add_node(6,  po=(25,6))
g.add_node(7)
g.add_node(8)
g.add_node(9)
g.add_node(10)
g.add_node(11)

g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(6,7)
g.add_edge(7,5)
g.add_edge(8,9)
g.add_edge(10,11)
po = nx.get_node_attributes(g, 'po')
labels = nx.get_edge_attributes(g, 'wieght')
pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g,pos,node_size=300)
nx.draw_networkx_edges(g,pos,edgelist=g.edges())
nx.draw_networkx_labels(g,pos)
print(g.nodes())
print(g.edges())
#nx.draw(g,with_labels=1)
mlp.show()

#nx.write_edgelist ( g , 'liste.txt' )
# nx.draw_networkx(g, with_labels=True)
# print(type(g), g)


#plt.show()
import networkx as fx
#graph = {'a': ['c'], 'b': ['c', 'e'], 'c': ['a', 'b', 'd', 'e'], 'd': ['c'], 'e': ['c', 'b'], 'f': []}

#G = fx.Graph()

#for k,v in graph.items():
   # G.add_node(k)
  #  for i in v:
 #       G.add_edge(k, i)

#fx.draw(G)

#plt.show()
