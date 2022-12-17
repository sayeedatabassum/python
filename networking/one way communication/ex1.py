import socket

if __name__ == '__main__' :

#creating a socket

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket created successfully')

    #binding the socket
    ip_address = 'localhost'
    port_no = 8888
    address = (ip_address,port_no)
    server_socket.bind(address)
    print(f'ip_address: {ip_address}')
    print(f'port_no: {port_no}')
    print(f'socket got binded to: {ip_address} running on to portno: {port_no}')
