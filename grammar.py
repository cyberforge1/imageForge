import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "ll_project.settings"
django.setup()
import openai
from dotenv import load_dotenv
from createPrompt import generatePrompt
from imageGeneration.models import Prompt

# Load the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


def rewrite_sentence(sentence):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"{sentence}\n\nRewrite this sentence:",
        temperature=0.5,
        max_tokens=60,
    )

    # Extract the rewritten sentence from the response
    rewritten = response.choices[0].text.strip()
    return rewritten


# Test the function
prompt = generatePrompt()
prompt_text = prompt
print(prompt_text)
rewritten_sentence = rewrite_sentence(prompt)
print(f"Original: {prompt}\nRewritten: {rewritten_sentence}")


prompt_model = Prompt()
prompt_model.text_field = rewritten_sentence
prompt_model.save()

prompt_id = prompt_model.prompt_id - 1


# Created to fetch the image prompt text that is displayed on the webpage
last_prompt_id = prompt_id

prompt_instance = Prompt.objects.get(prompt_id=last_prompt_id).text_field

print(prompt_instance)
print(prompt_instance)
