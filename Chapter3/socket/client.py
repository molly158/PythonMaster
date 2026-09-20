import socket

#1. 创建一个socket对象
socket_client=socket.socket()
#2. 连接服务器
socket_client.connect(('localhost',8880))
#3. 发送信息
while True:
    send_msg=input("saisie le message: ")
    if send_msg == "exit":
        break
    socket_client.send(send_msg.encode("UTF-8"))
    recv_data=socket_client.recv(1024)
    recv_data=recv_data.decode("UTF-8")
    print(f"le serveur repond en envoyant le message suivant: {recv_data}")

socket_client.close()