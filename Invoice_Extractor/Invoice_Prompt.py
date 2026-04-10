def build_invoice_prompt(invoice_text):

    return f"""
You are an AI system that extracts structured data from invoices.

Extract the following fields:

invoice_number
invoice_date
vendor_name
po_number
total_amount
currency

Return valid JSON.

Invoice text:

{invoice_text}
"""