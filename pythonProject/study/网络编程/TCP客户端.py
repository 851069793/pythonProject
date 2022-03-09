import socket
if __name__=="__main__":
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.131.62",8080))
    send_data = "我是客户端,请接收".encode("gbk")
    tcp_client_socket.send(send_data)
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data)
    print(recv_data.decode("gbk"))
    tcp_client_socket.close()
