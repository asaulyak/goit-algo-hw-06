import networkx as nx
import matplotlib.pyplot as plt
from faker import Faker
import random

fake = Faker()
social_network = nx.Graph()
user_num = 50

people = [fake.name() for _ in range(user_num)]

social_network.add_nodes_from(people)

for person in people:
    num_friends = random.randint(2, 10)  # Each person has 2 to 10 friends
    friends = random.sample(people, num_friends)
    for friend in friends:
        if person != friend:
            social_network.add_edge(person, friend)

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
plt.title("Social Network")
plt.axis('off')

nodes_num = social_network.number_of_nodes()
edges_num = social_network.number_of_edges()

plt.figtext(0.5, 0.05, f"Number of nodes: {nodes_num}, Number of edges: {edges_num}", ha="center", fontsize=10)

plt.show()

