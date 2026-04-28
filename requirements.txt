from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

def parse_with_ollama(dom_chunks, parse_description):
    model = Ollama(model="llama3")
    template = """You are a helpful assistant extracting data.
User wants to extract the following: {parse_description}
Content:
{dom_content}
Provide your response as clean structured text or tables.
"""
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)
    return "\n".join(parsed_results)
