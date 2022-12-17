import socket
import time

if __name__ == '__main__':
    
    try:  # creating a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket got created at client end')

        # establishing connection using connect()
        ip_address = 'localhost'
        port_no = 8888
        address = (ip_address, port_no)
        client_socket.connect(address)
        print(f'socket got connected to: {ip_address} running on to portno: {port_no}')
        print('new connection got establised')
        time.sleep(3)

        #to receive the response from the server
        bufsize = 1024
        recv_data = client_socket.recv(bufsize).decode('utf-8')
        print(f'the response from the server:{recv_data}')

        #sending the response to the server
        data = input('enter the msg to the server: ')
        client_socket.send(data.encode('utf-8'))

    except socket.error as msg:
        print(f'the cause of the exception:{msg}')

    finally:
        client_socket.close()
        print('client access socket got closed')
