import grpc
from concurrent import futures  # Import the futures module
import communication_pb2
import communication_pb2_grpc


class CommunicationServicer(communication_pb2_grpc.CommunicationServiceServicer):
    def __init__(self):
        self.clients = set()

    def SendMessage(self, request, context):
        message = request.text
        for client in self.clients:
            try:
                client.SendResponse(communication_pb2.Message(text=message))
            except:
                pass
        return communication_pb2.Message(text="Message sent to all clients")

def run_broker_server():
    print("Starting broker server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    communication_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Broker server is running...")
    server.wait_for_termination()


if __name__ == '__main__':
    run_broker_server()
