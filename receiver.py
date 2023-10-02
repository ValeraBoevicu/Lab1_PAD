import grpc
import communication_pb2
import communication_pb2_grpc
from concurrent import futures  # Import the futures module

class ReceiverServicer(communication_pb2_grpc.CommunicationServiceServicer):
    def __init__(self):
        self.received_messages = []

    def SendResponse(self, request, context):
        message = request.text
        self.received_messages.append(message)

def run_receiver_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServiceServicer_to_server(ReceiverServicer(), server)
    server.add_insecure_port('[::]:50052')  # Use a different port for the receiver
    server.start()
    print("Receiver is listening...")
    server.wait_for_termination()

if __name__ == '__main__':
    run_receiver_server()


