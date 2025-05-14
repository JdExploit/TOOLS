import subprocess

def boot_time_check():
    print("\n🕒 Últimos eventos de arranque (Windows):")
    cmd = 'wevtutil qe System "/q:*[System[(EventID=6005)]]" /f:text /c:5'
    resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(resultado.stdout)

def slow_services():
    print("\n🐌 Servicios con inicio automático que podrían retrasar el arranque:")
    cmd = 'powershell "Get-Service | Where-Object {$_.StartType -eq \'Automatic\' -and $_.Status -ne \'Running\'}"'
    resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(resultado.stdout)

if __name__ == "__main__":
    boot_time_check()
    slow_services()
