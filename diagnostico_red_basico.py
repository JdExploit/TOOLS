# diagnostico_red_basico.py
import subprocess
import socket
import platform

def ping_sitio(sitio):
    print(f"\n📡 Haciendo ping a: {sitio}")
    param = "-n" if platform.system() == "Windows" else "-c"
    resultado = subprocess.run(f"ping {param} 4 {sitio}", shell=True, capture_output=True, text=True)
    print(resultado.stdout)

def comprobar_dns(nombre):
    print(f"\n🔎 Resolviendo DNS de: {nombre}")
    try:
        ip = socket.gethostbyname(nombre)
        print(f"✅ {nombre} → {ip}")
    except socket.gaierror:
        print(f"❌ No se pudo resolver: {nombre}")

def diagnostico_basico():
    print("=== 🩺 Diagnóstico de Red Básico ===")

    sitios = [
        "outlook.office365.com",
        "teams.microsoft.com",
        "www.google.com",
        "8.8.8.8"
    ]

    for sitio in sitios:
        comprobar_dns(sitio)
        ping_sitio(sitio)

    print("\n✅ Diagnóstico básico finalizado.")

if __name__ == "__main__":
    diagnostico_basico()
