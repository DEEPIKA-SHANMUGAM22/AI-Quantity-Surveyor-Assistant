from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(area, cement, bricks, steel, total_cost):
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph("AI Quantity Surveyor Report", styles['Title']))
    content.append(Spacer(1, 20))

    # Table
    data = [
        ["Parameter", "Value"],
        ["Area", f"{round(area)} sq.ft"],
        ["Cement", f"{round(cement)} bags"],
        ["Bricks", f"{round(bricks)}"],
        ["Steel", f"{round(steel)} kg"],
        ["Total Cost", f"₹{round(total_cost)}"]
    ]

    table = Table(data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
    ]))

    content.append(table)
    content.append(Spacer(1, 15))
    content.append(Paragraph("Note: Estimates are approximate based on input plan.", styles['Italic']))

    doc.build(content)

    return "report.pdf"