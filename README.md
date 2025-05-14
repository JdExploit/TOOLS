# TOOLS

# 🛠 SysAdmin Toolkit – Scripts de Diagnóstico y Soporte

Colección de scripts en Python diseñados para **administradores de sistemas** (N1 a N3) en entornos empresariales. Cada script resuelve tareas comunes o repetitivas relacionadas con **problemas de red, conectividad, diagnósticos de Outlook, rendimiento del sistema, inventario, limpieza y más**.

> ✅ Enfocados en Windows, compatibles con terminales con permisos administrativos.

---

## 📦 Contenido del toolkit

| Script | Propósito | Nivel |
|--------|-----------|-------|
| `diagnostico_red_basico.py` | Diagnóstico rápido de red: ping, DNS, puertos clave (Outlook, web) | N1–N2 |
| `diagnostico_red_avanzado.py` | Diagnóstico profundo: traceroute, proxy, DNS, latencia | N3 |
| `bootcheck.py` | Verifica eventos de arranque y servicios lentos al inicio | N2–N3 |
| `inventario_software.py` | Lista el software instalado en la máquina | N2 |
| `limpieza_ip_dns.py` | Limpia caché DNS, renueva IP, resetea Winsock | N1 |
| `monitor_recursos.py` | Monitor en vivo de uso de CPU y RAM | N2 |
| `limpieza_temporales.py` | Borra archivos temporales para liberar espacio | N1 |

---

## 🚀 Uso

1. Instala Python 3.8+ en el equipo destino.
2. (Opcional) Crea un entorno virtual:  
   ```bash
   python -m venv venv && venv\Scripts\activate
