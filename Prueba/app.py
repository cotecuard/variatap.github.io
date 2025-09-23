from flask import Flask, render_template, redirect, url_for
from pathlib import Path
from datetime import datetime

# Ruta base = carpeta donde está este archivo
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Garantiza que exista /templates
TEMPLATES_DIR.mkdir(exist_ok=True)

app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

@app.route("/")
def index():
    return render_template("victor.html")

@app.route("/crear_html", methods=["POST"])
def crear_html():
    # Opcional: nombre único por timestamp para no sobrescribir
    fname = f"victor.html"
    file_path = TEMPLATES_DIR / fname

    nuevo_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>{fname}</title>
</head>
<body>
    <h1>Archivo creado dinámicamente 🚀</h1>
    <p>Generado: {datetime.now().isoformat(timespec='seconds')}</p>
    <p><a href="{{{{ url_for('index') }}}}">Volver al inicio</a></p>
</body>
</html>"""

    # Escribe el archivo en /templates
    file_path.write_text(nuevo_html, encoding="utf-8")

    # Redirige a una ruta que lo renderice
    return redirect(url_for("mostrar_nuevo", filename=fname))

@app.route("/nuevo/<filename>")
def mostrar_nuevo(filename):
    # Renderiza el HTML recién creado
    return render_template(filename)

if __name__ == "__main__":
    # Ejecuta siempre desde la carpeta del archivo para evitar rutas relativas raras
    import os
    os.chdir(BASE_DIR)
    app.run(debug=True)
