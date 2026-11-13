import socket
import time

LOCAL_HOST = "127.0.0.1"
LOCAL_PORT = 45678

# IP-адреса куди відправляємо потік (сюди можеш вписати IP твоєї ESP32 або залишити широкомовну/наступний ПК)
TARGET_IP = "192.168.144.50" 
TARGET_PORT = 8888

def main():
    print("=== Skyline-ESP32 Bridge Launcher ===")
    print("Спроба з'єднання з локальним API Skyline...")
    
    while True:
        try:
            local_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            local_sock.connect((LOCAL_HOST, LOCAL_PORT))
            print("[+] Успішно підключено до Skyline API!")

            net_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            while True:
                data = local_sock.recv(1024)
                if not data:
                    break
                net_sock.sendto(data, (TARGET_IP, TARGET_PORT))
        except Exception:
            # Якщо програма ще не запущена, тихо чекаємо і пробуємо знову
            time.sleep(2)

if __name__ == "__main__":
    main()