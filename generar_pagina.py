from pathlib import Path

# Crear carpetas
SITE_DIR = Path("sitio")
CSS_DIR = SITE_DIR / "css"

SITE_DIR.mkdir(exist_ok=True)
CSS_DIR.mkdir(exist_ok=True)

# ---- HTML ----
HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Internet Cuántico — Retro Futurista</title>
    <link rel="stylesheet" href="css/estilo.css">
</head>
<body>

<div class="grid-bg"></div>

<header>
    <h1>Internet Cuántico</h1>
    <p class="subtitulo">Documentación técnica — Estética Retro-Futurista</p>
</header>

<main>

<section>
    <h2>¿Qué es el Internet Cuántico?</h2>
    <p>
        Red basada en superposición, entrelazamiento y transmisión cuántica segura.
        Un paradigma que redefine la comunicación avanzada.
    </p>
</section>

<section>
    <h2>Aplicaciones</h2>
    <ul>
        <li>Distribución cuántica de claves (QKD).</li>
        <li>Computación cuántica remota.</li>
        <li>Sensores cuánticos distribuidos.</li>
        <li>Protocolos de comunicación imposibles de falsificar.</li>
    </ul>
</section>

<section>
    <h2>Retos Principales</h2>
    <ul>
        <li>Decoherencia cuántica.</li>
        <li>Desarrollo de repetidores fotónicos.</li>
        <li>Integración con redes clásicas.</li>
        <li>Infraestructura global estandarizada.</li>
    </ul>
</section>

</main>

<footer>
    <p>Generado automáticamente — Estética retro futurista</p>
</footer>

</body>
</html>
"""

# ---- CSS ----
CSS = """
/* --------- RETRO FUTURISTA MINIMAL --------- */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #070a14;
    color: #dfe7ff;
    overflow-x: hidden;
    min-height: 100vh;
}

/* Fondo cuadriculado tipo futurista */
.grid-bg {
    position: fixed;
    inset: 0;
    background:
        linear-gradient(#1b2335 1px, transparent 1px),
        linear-gradient(90deg, #1b2335 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: 0.12;
    z-index: -1;
}

/* HEADER estilo neón */
header {
    text-align: center;
    padding: 80px 20px 60px;
    background: radial-gradient(circle at 50% 30%, rgba(0,112,255,0.35), transparent 70%);
}

header h1 {
    font-size: 48px;
    color: #99caff;
    text-shadow: 0 0 8px #0084ff;
}

.subtitulo {
    font-size: 18px;
    opacity: 0.75;
    margin-top: 8px;
}

/* Tarjetas translúcidas */
main {
    width: 90%;
    max-width: 900px;
    margin: 20px auto 80px;
}

section {
    background: rgba(255,255,255,0.04);
    padding: 25px 30px;
    margin: 30px 0;
    border: 1px solid rgba(0,140,255,0.25);
    border-radius: 14px;
    backdrop-filter: blur(6px);
    box-shadow: 0 0 18px rgba(0,140,255,0.18);
    transition: 0.25s ease;
}

section:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 26px rgba(0,140,255,0.35);
}

h2 {
    color: #78b6ff;
    margin-bottom: 12px;
    text-shadow: 0 0 6px #0066ff;
}

ul {
    padding-left: 22px;
    margin-top: 10px;
}

li {
    margin: 8px 0;
}

/* FOOTER */
footer {
    text-align: center;
    padding: 30px;
    opacity: 0.65;
    font-size: 14px;
}
"""

# Guardar los archivos
(SITE_DIR / "index.html").write_text(HTML, encoding="utf-8")
(CSS_DIR / "estilo.css").write_text(CSS, encoding="utf-8")

print("Página RETRO FUTURISTA generada correctamente en 'sitio/'.")