from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

from PO_Extractor.PO_Schema import PO_Schema
from PO_Extractor.PO_Prompt import build_PO_Prompt
from Invoice_Extractor.Invoice_Text_Extractor import extract_text_from_pdf

llm=ChatOpenAI(model="gpt-4o-mini")

parser=PydanticOutputParser(pydantic_object=PO_Schema)

def extract_purchase_order_details(pdf_path):

    pdf_text=extract_text_from_pdf(pdf_path)
    prompt=build_PO_Prompt(pdf_text)

    full_prompt=prompt+"\n"+parser.get_format_instructions()
    response=llm.invoke(full_prompt)
    structured_output = parser.parse(response.content)

    return structured_output
