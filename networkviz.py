from turtle import color
from pyvis.network import Network 
import networkx as nx
import matplotlib.pyplot as plt

net = Network()
G = nx.Graph()

pages = ['Home Page']

g1_size = 12
g2_size = 9
g3_size = 6
g4_size = 3

G.add_node(1, label="Home Page", title="XIS Landing Page", color='#000000', size= 12, group=1)
G.add_node(2, label="About Page", title="XIS About Page", color='#880808', size= 9, group=2)
G.add_node(3, label="Cancel Page", title="Cancel Order Page", color='red', size= 6, group=3)
G.add_node(10, label="Success Page", title="Successful Purchase Page", size= 6, color='#3BC14A', group=3)
G.add_node(4, label="Contact", title="Contact Page With Feedback Form", size= 9, color='#6DD87D', group=2)
G.add_node(5, label="Feedback Viewer", title="View Customer Feedback Application", size= 3, color='#0BE12B', group=4)
G.add_node(6, label="Login", title="Login to XIS Backend", size=3 , color='#CFCFCF', group=4)
G.add_node(7, label="Sell Page", title="Sell Hydroponics Unit Page", size= 9, color='#3BC14A', group=2)
G.add_node(8, label="Customer Data Viewer", title="View Customers Application", size= 3, color='#6DD87D', group=4)
G.add_node(9, label="Individual Customer Order Data", title="View Customer Order Data Application", size= 3, color='#6DD87D', group=4)

G.add_edges_from([(1, 2, {'weight': g1_size}), (1, 4, {'weight': g1_size}), (1, 7, {'weight': g1_size}), (1, 6, {'weight': g1_size})])

G.add_edges_from( [ (7, 10, {'weight': g2_size, 'color': '#3BC14A'}), (7, 3, {'weight': g2_size, 'color': '#3BC14A'}) ] )

G.add_edges_from( [ (6, 8, {'weight': g4_size, 'color': '#CFCFCF'}), (6, 5, {'weight': g4_size, 'color': '#CFCFCF'}) ] )

G.add_edges_from([(8, 9, {'weight': g4_size, 'color': '#6DD87D'})])

G.add_edges_from( [ (3, 1, {'weight': g3_size, 'color': 'red'}), (10, 1, {'weight': g3_size, 'color': '#3BC14A'})] )

#G.add_edges_from( [ (8, 9, {'weight': g4_size, 'color': '#6DD87D'}), (6, 5, {'weight': g4_size, 'color': '#CFCFCF'}) ] )


nt = Network('500px', '500px')

nt.from_nx(G)

nt.show('nx.html')

