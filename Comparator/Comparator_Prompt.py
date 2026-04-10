def build_comparison_prompt(invoice_data,po_data):
    return f"""
    Compare the invoice and purchase order.

    Determine:

    1. Does PO number match?
    2. Does amount match?
    3. Does currency match?
    4. What is the difference in amount?

    Invoice data:

    {invoice_data}

    PO data:

    {po_data}

    Return structured JSON.
    """