import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from .schema import ResumeSchema

load_dotenv()

# Initialize Gemini 2.5 Flash
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

# Pydantic Output Parser (modern replacement)
parser = PydanticOutputParser(pydantic_object=ResumeSchema)

prompt_template = PromptTemplate(
    input_variables=["text"],
    template=(
        "Extract structured resume data from the text below.\n\n"
        "{text}\n\n"
        "{format_instructions}"
    ),
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

def extract_resume_data(text: str) -> ResumeSchema:
    prompt = prompt_template.format(text=text)

    response = llm.invoke(prompt)

    try:
        return parser.parse(response.content)
    except Exception:
        return ResumeSchema(**{k: None for k in ResumeSchema.__annotations__.keys()})
