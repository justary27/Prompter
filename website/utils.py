# views.py
import json
from openai import OpenAI
from django.conf import settings
import os

def generate_schema(model: str, prompt: str) -> str:
    try:
        base_path = os.path.join(os.path.dirname(__file__),)
        json_path = ""

        match model:
            case "gemini":
                json_path = os.path.join(base_path, 'gemini.json')
            case "claude":
                json_path = os.path.join(base_path, 'claude.json')
            case "phinde":
                json_path = os.path.join(base_path, 'phind.json')
            case _:
                raise ValueError("Invalid model")

        with open(json_path) as file:
            data = json.load(file)

        request_data = data["request"]
        response_data = data["response"]

        # Create a prompt for generating the request schema
        prompt = f"""
        Below is a request sent to an llm model with a prompt. You are given the api request and response got from the api.
        Generate a python code for sending a request to the api for a new prompt:

        Provided prompt (used in request): Describe asiatic lions in brief.
        Request: {json.dumps(request_data, indent=2)}
        Response: {json.dumps(response_data, indent=2)}
        Prompt (to use in request schema): {prompt}
        
        Follow these points while giving your answer:
        1. Infer the url to which to send, the headers that should be used. 
        2. Infer the method of the request, the body of the request, the response schema. 
        3. If the body is sent in some json encoding, infer it and make the body appropriate for the new prompt.

        4. Identify which headers, tokens and cookies may need replacement/updation while sending request and specify 
        the replacements needed as described in (4.) for example, say a header "token" needs to be changed, 
        specify it like token : $TOKEN in the header. Do similarly for cookies and tokens in body as well as headers.
        """

        # !!! Important set your API key here in .env file before sending the request
        # Set the OpenAI API key
        client = OpenAI(os.getenv("OPENAI_KEY"))



        # Send the prompt to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "The following is a conversation with an AI assistant. The assistant helps in drawing out request given input jsons of request and response dat of AI LLMs."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=4096,
        )

        # Get the generated schema
        schema = response.choices[0].message.content

        # Return the schema as JSON response
        return schema

    except Exception as e:
        return str(e)
