from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Almacén temporal: una lista de Python (se pierde al reiniciar el servidor).
# En la Etapa 3 esto se reemplaza por una base de datos.
vulnerabilities = [
    {"id": 1, "title": "SQL Injection", "category": "A03 - Injection", "severity": "High"},
    {"id": 2, "title": "Cross-Site Scripting", "category": "A03 - Injection", "severity": "Medium"},
    {"id": 3, "title": "Broken Access Control", "category": "A01 - Broken Access Control", "severity": "High"},
]

OWASP_CATEGORIES = [
    "A01 - Broken Access Control",
    "A02 - Cryptographic Failures",
    "A03 - Injection",
    "A04 - Insecure Design",
    "A05 - Security Misconfiguration",
    "A06 - Vulnerable and Outdated Components",
    "A07 - Identification and Authentication Failures",
    "A08 - Software and Data Integrity Failures",
    "A09 - Security Logging and Monitoring Failures",
    "A10 - Server-Side Request Forgery",
]

SEVERITIES = ["Low", "Medium", "High", "Critical"]


@app.route("/", methods=["GET", "POST"])
def index():
    """Pantalla 1: formulario Vulnerability Log."""
    error = None
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        category = request.form.get("category", "")
        severity = request.form.get("severity", "")

        if not title:
            error = "Escribe un título para la vulnerabilidad."
        elif category not in OWASP_CATEGORIES or severity not in SEVERITIES:
            error = "Selecciona una categoría y una severidad válidas."
        else:
            vulnerabilities.append({
                "id": len(vulnerabilities) + 1,
                "title": title,
                "category": category,
                "severity": severity,
            })
            return redirect(url_for("reports"))

    return render_template(
        "index.html",
        categories=OWASP_CATEGORIES,
        severities=SEVERITIES,
        error=error,
    )


@app.route("/reports")
def reports():
    """Pantalla 2: tabla Reported vulnerabilities."""
    return render_template("reports.html", vulnerabilities=vulnerabilities)


if __name__ == "__main__":
    app.run(debug=True)