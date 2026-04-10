from pydantic import BaseModel

class ComparisonResult(BaseModel):
    po_match:bool
    amount_match: bool
    currency_match: bool
    difference: float
    confidence: float

