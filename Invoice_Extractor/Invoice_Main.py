from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

from Invoice_Extractor.Invoice_Text_Extractor import extract_text_from_pdf
from Invoice_Extractor.Invoice_Prompt import build_invoice_prompt
from Invoice_Extractor.Invoice_Schema import InvoiceExtractorSchema
llm=ChatOpenAI(model="gpt-4o-mini")

parser = PydanticOutputParser(pydantic_object=InvoiceExtractorSchema)

def extract_invoice_data(pdf_path):

    pdf_text=extract_text_from_pdf(pdf_path)
    prompt=build_invoice_prompt(pdf_text)
    full_prompt=prompt+"\n"+parser.get_format_instructions()
    response=llm.invoke(full_prompt)
    structured_output = parser.parse(response.content)

    return structured_output

