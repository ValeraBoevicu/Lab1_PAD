import grpc
import communication_pb2
import communication_pb2_grpc

def send_message(message_text):
    channel = grpc.insecure_channel('localhost:50053')
    stub = communication_pb2_grpc.CommunicationServiceStub(channel)
    message = communication_pb2.Message(text=message_text)
    response = stub.SendMessage(message)
    return response

if __name__ == '__main__':
    while True:
        message_text = input("Enter a message to send (or 'exit' to quit): ")
        if message_text.lower() == 'exit':
            break
        response = send_message(message_text)
        print("Sender sent message:", message_text)
        print("Sender received response:", response.text)

