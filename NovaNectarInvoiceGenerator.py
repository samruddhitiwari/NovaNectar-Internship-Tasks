from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_invoice(invoice_number, date, bill_to, items, output_filename):
    print("Starting to generate invoice...")
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter
    
    # Invoice Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, height - 50, "INVOICE")
    
    # Invoice Number and Date
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 80, f"Invoice Number: {invoice_number}")
    c.drawString(30, height - 100, f"Date: {date}")
    
    # Bill To
    c.drawString(30, height - 140, "Bill To:")
    for i, line in enumerate(bill_to.split('\n')):
        c.drawString(30, height - 160 - (i * 20), line)
    
    # Table Header
    c.drawString(30, height - 220, "Item")
    c.drawString(300, height - 220, "Quantity")
    c.drawString(400, height - 220, "Price")
    c.drawString(500, height - 220, "Total")
    
    # Table Content
    total_price = 0
    y = height - 240
    for item, quantity, price in items:
        total = quantity * price
        total_price += total
        
        c.drawString(30, y, item)
        c.drawString(300, y, str(quantity))
        c.drawString(400, y, f"${price:.2f}")
        c.drawString(500, y, f"${total:.2f}")
        
        y -= 20
    
    # Total Amount
    c.drawString(400, y - 20, "Total Amount:")
    c.drawString(500, y - 20, f"${total_price:.2f}")
    
    c.showPage()
    c.save()
    print("Invoice generated and saved as:", output_filename)

# Example usage
invoice_number = "12345"
date = "2024-06-30"
bill_to = "John Doe\n123 Main Street\nCity, State, ZIP"
items = [
    ("Item 1", 2, 30.00),
    ("Item 2", 1, 50.00),
    ("Item 3", 3, 20.00)
]
output_filename = "invoice.pdf"

generate_invoice(invoice_number, date, bill_to, items, output_filename)
