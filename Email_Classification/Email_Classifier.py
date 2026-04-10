from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

from Email_Classification.Email_Prompt import build_email_prompt
from Email_Classification.Email_Schema import EmailClassification

llm=ChatOpenAI(model="gpt-4o-mini")
parser= PydanticOutputParser(pydantic_object=EmailClassification)

def classify_email(email_text):

    prompt=build_email_prompt(email_text)
    enhanced_prompt=prompt+"\n"+parser.get_format_instructions()
    response=llm.invoke(enhanced_prompt)
    structured_output = parser.parse(response.content)

    return structured_output



