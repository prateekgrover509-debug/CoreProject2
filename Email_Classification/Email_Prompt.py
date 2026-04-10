def build_email_prompt(email_text):

    return f"""
Classify the email into one of the categories:

pricing dispute
missing po
duplicate invoice
payment status query
general query

Also determine:

priority:
low
medium
high

Decide:

requires_invoice_extraction (true/false)
requires_po_check (true/false)

Return structured JSON only.

Email:

{email_text}
"""