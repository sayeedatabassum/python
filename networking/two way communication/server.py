import socket
import time

if __name__ == '__main__':

    try: #creating a socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket got created at server end')

        #binding the socket
        ip_address = 'localhost'
        port_no = 8888
        address = (ip_address,port_no)
        server_socket.bind(address)
        print(f'socket got binded to: {ip_address} running on to portno: {port_no}')

        #making the server socket to listen to the request
        backlog = 5
        server_socket.listen(backlog)
        print(f'the server socket con listen to: {backlog} request')


        #accepting the request came from client and sending the response
        client_access,(ip_address,port_no) = server_socket.accept()
        print(f'server socket got connected to client socket whose ip_address:{ip_address} running to port no: {port_no}')

        #sending response to the client
        data = input('enter the msg for the client: ')
        client_access.send(data.encode('utf-8'))

        bufsize = 1024
        recv_data = client_access.recv(bufsize).decode('utf-8')
        print(f'the response from the server:{recv_data}')
        time.sleep(3)

    except socket.error as msg:
        print(f'the cause of the exception:{msg}')

    finally:
        client_access.close()
        print('client access socket got closed')
            
                
 