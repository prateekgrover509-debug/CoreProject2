from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

from Comparator.Comparator_Schema import ComparisonResult
from Comparator.Comparator_Prompt import build_comparison_prompt

llm=ChatOpenAI(model="gpt-4o-mini")

parser = PydanticOutputParser(pydantic_object=ComparisonResult)

def compare_invoice_po(invoice_data,po_data):

    prompt=build_comparison_prompt(invoice_data,po_data)
    full_prompt=prompt+"\n"+parser.get_format_instructions()

    response=llm.invoke(full_prompt)
    structured_output=parser.parse(response.content)
    return structured_output
