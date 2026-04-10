from pydantic import BaseModel

class PO_Schema(BaseModel):
    po_number: str

    vendor_name: str

    po_date: str

    approved_amount: str

    currency: str

    confidence: float

