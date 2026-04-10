from pydantic import BaseModel

class EmailClassification(BaseModel):
    category: str

    priority: str

    requires_invoice_extraction: bool

    requires_po_check: bool

    confidence: float

