
from datetime import datetime
from pathlib import Path
import subprocess
import shutil
import sys

# Rutas del proyecto
BASE_DIR = Path(__file__).parent
CARPETA_REPORTES = BASE_DIR / "reportes"
CARPETA_HISTORIAL = CARPETA_REPORTES / "historial"

# Crear carpetas si no existen
CARPETA_HISTORIAL.mkdir(parents=True, exist_ok=True)

# Fecha y hora para identificar cada ejecución
fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Nombre del reporte histórico
reporte_historico = (
    CARPETA_HISTORIAL / f"reporte-qa-{fecha_hora}.html"
)

# Ejecutar las pruebas y generar el reporte
resultado = subprocess.run([
    sys.executable,
    "-m",
    "pytest",
    "automatizacion/",
    "-v",
    f"--html={reporte_historico}",
    "--self-contained-html"
], cwd=BASE_DIR)

# Actualizar el reporte principal
if reporte_historico.exists():
    reporte_actual = CARPETA_REPORTES / "reporte-qa.html"
    shutil.copy2(reporte_historico, reporte_actual)

    print("\nReporte principal actualizado:")
    print(reporte_actual)

    print("\nReporte guardado en el historial:")
    print(reporte_historico)

sys.exit(resultado.returncode)
