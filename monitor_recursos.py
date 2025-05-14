import psutil
import time

def monitor():
    print("⏱️ Monitor en tiempo real (Ctrl+C para salir)\n")
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        print(f"CPU: {cpu}% | RAM: {ram}%")
        time.sleep(1)

if __name__ == "__main__":
    monitor()
