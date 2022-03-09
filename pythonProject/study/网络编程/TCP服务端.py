import socket
if __name__ == "__main__":
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    tcp_server_socket.bind(("",8989))
    tcp_server_socket.listen(128)
    service_client_socket,ip_port = tcp_server_socket.accept()
    print("客户端的ip地址以及端口号:",ip_port)
    recv_data = service_client_socket.recv(1024)
    print(recv_data.decode("gbk"))
    send_data = "ok,已收到请求".encode("gbk")
    service_client_socket.send(send_data)
    service_client_socket.close()
    tcp_server_socket.close()
