import flower as flower
from keras.utils import to_categorical
from keras.datasets import mnist
import model as model
import grpc
import subprocess
from concurrent import futures

print("\n\n")
print("\n\n")
print("\n\n")

import service_pb2 
import service_pb2_grpc

class MyService(service_pb2._MYSERVICE): 
    #@flower.rpc
    def SendDataset(self, y_cat_train) ->str:
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        y_cat_test = to_categorical(y_test, num_classes=10)
        y_cat_train = to_categorical(y_train, 10)
        print("hi")
        #client.FederatedLearningClient.send_dataset(y_cat_train)

def start_stop():
    print("hii")
    #server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #service_pb2.add_MyServiceServicer_to_server(MyService(), server)
    #server.add_insecure_port('0.0.0.0:50051')
    #server.start()
    print("gRPC Server started at 0.0.0.0:50051")
    #federe_model = model.learning(x_train, y_cat_train, x_test, y_cat_test)
    # training the model
    #model.learning_metrics(federe_model, x_test, y_cat_test, y_test)
    # get metrics from trained model
    #SendDataset(y_cat_train)
    # send dataset
    
    # Shut down the server
    #server.stop()

# The detached=True option runs the containers in the background.
subprocess.run(["docker-compose", "up", "-d"])
# call class definiton for service
start_stop()
#stops and removes the containers
subprocess.run(["docker-compose", "down"])