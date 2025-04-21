from collections import deque

import networkx as nx
import matplotlib.pyplot as plt
from faker import Faker
import random

from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra

fake = Faker()
social_network = nx.Graph()
user_num = 10

people = [fake.name() for _ in range(user_num)]

social_network.add_nodes_from(people)

for person in people:
    num_friends = random.randint(2, 10)  # Each person has 2 to 10 friends
    friends = random.sample(people, num_friends)
    for friend in friends:
        if person != friend:
            weight = round(random.uniform(0.1, 1.0), 2)
            social_network.add_edge(person, friend, weight=weight)

plt.figure(figsize=(14, 14))
pos = nx.spring_layout(social_network, seed=42)
nx.draw_networkx(
    social_network,
    pos,
    with_labels=True,
    node_color='skyblue',
    edge_color='gray',
    node_size=500,
    font_size=8
)

labels = nx.get_edge_attributes(social_network, 'weight')
nx.draw_networkx_edge_labels(social_network, pos, edge_labels=labels)

plt.title("Social Network")
plt.axis('off')

nodes_num = social_network.number_of_nodes()
edges_num = social_network.number_of_edges()

plt.figtext(0.5, 0.05, f"Number of nodes: {nodes_num}, Number of edges: {edges_num}", ha="center", fontsize=10)

social_dfs_edges = dfs(social_network, people[0])

social_bfs_edges = bfs(social_network, deque([people[0]]))

print(list(social_dfs_edges))
print(list(social_bfs_edges))


dijkstra_distances = dijkstra(social_network, people[0])
print(dijkstra_distances)



plt.show()