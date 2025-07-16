from src.llm.ollama_llm import chain
from src.utils import utils

if __name__ == "__main__":
    cv_text = utils.read_pdf_text("cv.pdf")
    response = chain.invoke(
        {
            "cv_text": cv_text,
            "target_role": "Senior Full Stack Engineer",
            "target_location": "New York, USA",
            "candidate_goals": "Obtain a software engineering position in the U.S. with H-1B visa sponsorship",
            "experience_level": "Mid-level developer with 4 years of backend experience and some frontend exposure",
            "tech_stack": "Python, FastAPI, AWS, Docker, React, RabbitMQ, PostgreSQL",
            "additional_info": "Colombian citizen, currently living in Australia, fluent in English, willing to relocate immediately",
        }
    )
    print(response)
