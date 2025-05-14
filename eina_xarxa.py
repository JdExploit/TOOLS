import subprocess
import socket

def nslookup(target):
    try:
        result = subprocess.run(['nslookup', target], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error en nslookup: {e}"

def get_ip_info(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror as e:
        return f"Error al obtener IP: {e}"

def traceroute(host):
    try:
        result = subprocess.run(['tracert', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error en traceroute: {e}"

def check_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    mode = input("¿Desea consultar un nombre de dominio (1) o una dirección IP (2)? Introduzca 1 o 2: ")
    
    if mode not in ['1', '2']:
        print("Opción no válida. Salida del programa.")
        return

    target = input("Introduce el nombre de dominio o IP a consultar: ")
    
    # Realizar nslookup
    nslookup_result = nslookup(target)
    print("Resultado de nslookup:")
    print(nslookup_result)

    # Obtener IP
    ip_info = get_ip_info(target)
    print(f"IP de {target}: {ip_info}")

    # Realizar traceroute
    traceroute_result = traceroute(target)
    print("Resultado de traceroute:")
    print(traceroute_result)

    # Comprobar puertos
    ports_to_check = [80, 443, 22, 21]  # Puertos comunes
    open_ports = check_ports(ip_info, ports_to_check)
    print(f"Puertos abiertos en {ip_info}: {open_ports}")

if __name__ == "__main__":
    main()
