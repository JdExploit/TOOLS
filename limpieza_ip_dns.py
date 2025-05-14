import subprocess

def renovar_ip_dns():
    print("\n🔄 Renovando IP y limpiando caché DNS...")
    comandos = [
        "ipconfig /release",
        "ipconfig /renew",
        "ipconfig /flushdns",
        "nbtstat -R",
        "nbtstat -RR",
        "netsh int ip reset",
        "netsh winsock reset"
    ]

    for cmd in comandos:
        print(f"Ejecutando: {cmd}")
        resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(resultado.stdout)

if __name__ == "__main__":
    renovar_ip_dns()
