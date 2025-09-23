from flask import Flask, render_template, redirect, url_for
from pathlib import Path
from datetime import datetime
import os

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
TEMPLATES_DIR.mkdir(exist_ok=True)

app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/crear_html", methods=["POST"])
def crear_html():
    fname = f"nuevo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    file_path = TEMPLATES_DIR / fname
    nuevo_html = f"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="utf-8"><title>{fname}</title></head>
<body>
  <h1>Archivo creado dinámicamente 🚀</h1>
  <p>Generado: {datetime.now().isoformat(timespec='seconds')}</p>
  <p><a href="{{{{ url_for('index') }}}}">Volver al inicio</a></p>
</body>
</html>"""
    file_path.write_text(nuevo_html, encoding="utf-8")
    return redirect(url_for("mostrar_nuevo", filename=fname))

@app.route("/nuevo/<filename>")
def mostrar_nuevo(filename):
    return render_template(filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
