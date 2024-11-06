import socket

# Conversion factors
conversion_factors = {
    'cm': 1,
    'mm': 10,
    'inches': 0.393701,
    'km': 0.00001,
    'ft': 0.0328084,
    'm': 0.01,
    'yd': 0.0109361,
    'mile': 0.0000062137,
    'dm': 0.1
}

# Conversion logic
def convert_distance(value, from_unit, to_unit):
    if from_unit in conversion_factors and to_unit in conversion_factors:
        # Perform conversion
        converted_value = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        # Round the result to 2 decimal places (or change as needed)
        return round(converted_value, 2)
    return None

# TCP Server
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5002))
    server_socket.listen(1)

    print("TCP Server listening on port 5002")
    while True:
        client_socket,addr= server_socket.accept()
        data = client_socket.recv(1024).decode()
        value, from_unit, to_unit = data.split(',')
        converted_value = convert_distance(float(value), from_unit, to_unit)

        print(f"TCP Request from {addr[0]}: {value} {from_unit} to {to_unit}")
        client_socket.sendall(str(converted_value).encode())
        client_socket.close()

# UDP Server
def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 5001))

    print("UDP Server listening on port 5001")
    while True:
        data, addr = server_socket.recvfrom(1024)
        value, from_unit, to_unit = data.decode().split(',')
        converted_value = convert_distance(float(value), from_unit, to_unit)
        print(f"UDP Request from {addr[0]}: {value} {from_unit} to {to_unit}")
        server_socket.sendto(str(converted_value).encode(), addr)

if __name__ == '__main__':
    import threading
    # Start TCP and UDP servers in separate threads
    tcp_thread = threading.Thread(target=tcp_server, daemon=True)
    udp_thread = threading.Thread(target=udp_server, daemon=True)

    tcp_thread.start()
    udp_thread.start()

    tcp_thread.join()
    udp_thread.join()

    import threading
    # Start TCP and UDP servers in separate threads
    tcp_thread = threading.Thread(target=tcp_server, daemon=True)
    udp_thread = threading.Thread(target=udp_server, daemon=True)

    tcp_thread.start()
    udp_thread.start()

    tcp_thread.join()
    udp_thread.join()