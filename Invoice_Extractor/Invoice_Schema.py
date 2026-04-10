from pydantic import BaseModel

class InvoiceExtractorSchema(BaseModel):

    invoice_number: str
    invoice_date: str
    vendor_name: str
    po_number: str
    total_amount: str
    currency: str
    confidence: float
