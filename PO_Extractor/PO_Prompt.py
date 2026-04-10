def build_PO_Prompt(text):
    return f"""
    Extract purchase order details.

    Fields:

    po_number
    vendor_name
    po_date
    approved_amount
    currency

    Return JSON only.

    PO text:

    {text}
    """