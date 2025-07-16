from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from src.prompts import cv_analizer_template

prompt = PromptTemplate(
    input_variables=[
        "cv_text",
        "target_role",
        "target_location",
        "candidate_goals",
        "experience_level",
        "tech_stack",
        "additional_info",
    ],
    template=cv_analizer_template.template,
)
llm = OllamaLLM(model="llama3.2")
chain = prompt | llm
