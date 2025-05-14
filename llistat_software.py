import subprocess

def listado_software():
    print("\n📦 Listado de programas instalados (puede tardar)...")
    cmd = 'powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher | Format-Table -AutoSize"'
    resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(resultado.stdout)

if __name__ == "__main__":
    listado_software()
