import os
import shutil
import tempfile

def limpiar_temporales():
    temp_path = tempfile.gettempdir()
    print(f"🧹 Borrando archivos temporales de: {temp_path}")
    for root, dirs, files in os.walk(temp_path):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except:
                pass
    print("✅ Limpieza completada.")

if __name__ == "__main__":
    limpiar_temporales()
