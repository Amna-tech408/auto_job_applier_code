# import os
# import openai
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_cover_letter(resume, title, company, location):
#     prompt = (
#         f"Given this resume:\n{resume}\n\n"
#         f"Write a professional cover letter for the position of {title} at {company} in {location}."
#     )
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['choices'][0]['message']['content']
