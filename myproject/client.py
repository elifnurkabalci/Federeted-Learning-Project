import flower as flower
import numpy as np
import grpc
from grpc import ClientCallDetails
import subprocess

class FederatedLearningClient():
    def __init__(self):
        # Create a Flower client for each client system
        self.clients = []
        for i in range(3):
            self.clients.append(self)

    #@flower.rpc
    def send_dataset(self, dataset) ->str:
        w = np.random.randint(1, 100, 10)
        first_node, second_node, third_node = np.split(dataset, 3)

        for i in range(len(first_node)):
            node1 = first_node[i]
            node2 = second_node[i]
            node3 = third_node[i]
            node1 = node1 + w # delta(w0-1)
            node2 = node2 + w # delta(w0-2)
            node3 = node3 + w # delta(w0-3)

            delta_w = (node1 + node2 + node3)/3
            w = delta_w

        return delta_w



