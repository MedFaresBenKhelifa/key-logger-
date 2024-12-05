import socket

def receive_log_file():
    try:
        log_file_path = r"D:\log.txt"
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("192.168.1.169", 12346))
            s.listen()
            print("Server listening for connections...")
            conn, addr = s.accept()
            with conn:
                print("Connected by", addr)
                data = conn.recv(1024)
                with open(log_file_path, "ab") as f:
                    while data:
                        f.write(data)
                        data = conn.recv(1024)
            print("Log file received successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    receive_log_file()
