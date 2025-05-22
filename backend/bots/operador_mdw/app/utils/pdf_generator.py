from fpdf import FPDF
from datetime import datetime

def generar_pdf_estado(plataforma, safe_encoding=True):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    texto = (
        f"Informe de estado para la plataforma {plataforma}\n\n"
        f"Todo funciona correctamente.\n\n"
        f"Generado: {fecha}"
    )

    # Reemplazar emojis si se requiere codificación segura (forzado a True por defecto)
    if safe_encoding:
        texto = texto.encode('ascii', 'ignore').decode('ascii')

    pdf.multi_cell(0, 10, texto)

    filename = f"/app/estado_{plataforma.lower()}.pdf"
    try:
        pdf.output(name=filename)
    except Exception as e:
        print(f"Error al generar el PDF: {e}")

def registrar_envio_documento(bot_id: int):
    # Placeholder de lógica futura para registrar envío de documentos en base de datos
    print(f"[INFO] Documento enviado por bot_id={bot_id} registrado.")