from openai import OpenAI
import json


class OpenAIService:
    def __init__(self):
        self.client = OpenAI()

    def extract_review_pros_and_cons(self, review_content):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant, designed to analyze video game reviews and return pros and cons.",
                },
                {
                    "role": "system",
                    "content": "You will output your response in JSON. The response output will be a JSON with fields 'pros' and 'cons'",
                },
                {
                    "role": "system",
                    "content": "The JSON response output will have fields 'pros' and 'cons'. The values will be comma seperated pythonic lists of the pros and cons",
                },
                {
                    "role": "system",
                    "content": "The list of pros and cons should be generated ONLY from the content passed by the user. Do not use additional resources",
                },
                {"role": "user", "content": review_content},
            ],
        )
        print(
            f"Completion usage: Completion tokens: {completion.usage.completion_tokens}"
        )
        print(f"Completion usage: Prompt tokens: {completion.usage.prompt_tokens}")

        print(f"OpenAI finish reasons: {completion.choices[0].finish_reason} ")

        pros_cons_json = json.loads(completion.choices[0].message.content)

        return pros_cons_json
