import pandas as pd

from langchain_openai import ChatOpenAI


llm = ChatOpenAI(model="gpt-4o-mini")


def load_policy_data():

    df = pd.read_csv("SampleCSV.csv")

    knowledge_text = ""

    for _, row in df.iterrows():

        knowledge_text += f"{row['topic']} : {row['content']}\n"

    return knowledge_text


def policy_lookup(query):

    knowledge = load_policy_data()

    prompt = f"""
Answer the query using policy knowledge.

Knowledge:

{knowledge}

Query:

{query}
"""

    response = llm.invoke(prompt)

    return response.content