# diagnostico_red_avanzado.py
import subprocess
import platform
import socket
import os
import re

sitios_clave = [
    "outlook.office365.com",
    "teams.microsoft.com",
    "www.google.com",
    "8.8.8.8"
]

def ejecutar_comando(comando):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return resultado.stdout.strip()

def traceroute(dominio):
    print(f"\n📍 Traceroute a {dominio}:")
    if platform.system() == "Windows":
        print(ejecutar_comando(f"tracert -d -h 10 {dominio}"))
    else:
        print(ejecutar_comando(f"traceroute -n -m 10 {dominio}"))

def ping(dominio):
    print(f"\n⏱️ Ping a {dominio}:")
    param = "-n" if platform.system() == "Windows" else "-c"
    print(ejecutar_comando(f"ping {param} 4 {dominio}"))

def dns_usado():
    print("\n🧭 Servidores DNS configurados:")
    if platform.system() == "Windows":
        salida = ejecutar_comando("ipconfig /all")
        dns = re.findall(r"Servidores DNS[^\n]*\n(?:\s{20,}[\d\.]+\n?)+", salida)
        print('\n'.join(dns) if dns else "❌ No se encontró DNS configurado.")
    else:
        print(ejecutar_comando("cat /etc/resolv.conf"))

def proxy_config():
    print("\n🔐 Configuración de proxy:")
    if platform.system() == "Windows":
        salida = ejecutar_comando("reg query \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\"")
        proxy_enabled = re.search(r"ProxyEnable\s+REG_DWORD\s+0x1", salida)
        proxy_server = re.search(r"ProxyServer\s+REG_SZ\s+(.+)", salida)
        if proxy_enabled and proxy_server:
            print(f"✅ Proxy activo: {proxy_server.group(1)}")
        else:
            print("⚠️ No hay proxy configurado o está desactivado.")
    else:
        proxy_env = os.environ.get("http_proxy") or os.environ.get("https_proxy")
        if proxy_env:
            print(f"✅ Proxy por entorno: {proxy_env}")
        else:
            print("⚠️ No se detectó proxy configurado.")

def diagnostico_avanzado():
    print("=== 🧪 Diagnóstico de Red Avanzado (N3) ===\n")

    dns_usado()
    proxy_config()

    for sitio in sitios_clave:
        ping(sitio)
        traceroute(sitio)

    print("\n✅ Diagnóstico avanzado finalizado.")

if __name__ == "__main__":
    diagnostico_avanzado()
