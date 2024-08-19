from openai import OpenAI
import json


class OpenAIService:
    def __init__(self):
        self.client = OpenAI()

    def extract_review_pros_and_cons(self, review_content):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
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

    def assign_score_to_content(self, content):
        """
        Content should be a string with game review content.

        Returns a dictionary with an 'score' key and an int value.

        """

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant, designed to analyze video game reviews and return a score out of 10.",
                },
                {
                    "role": "system",
                    "content": "You will output your response as a single digit number between one and ten. The response output will be a JSON with field 'score'",
                },
                {
                    "role": "system",
                    "content": "The score outputed must be a single digit number between one and ten",
                },
                {
                    "role": "system",
                    "content": "The score given will be based on the contents of the review. A higher score will be given if a review has positive sentiment, and lower if a review has more negative sentiment",
                },
                {"role": "user", "content": content},
            ],
        )
        print(
            f"Completion usage: Completion tokens: {completion.usage.completion_tokens}"
        )
        print(f"Completion usage: Prompt tokens: {completion.usage.prompt_tokens}")

        print(f"OpenAI finish reasons: {completion.choices[0].finish_reason} ")

        scores_json = json.loads(completion.choices[0].message.content)

        if not scores_json or type(scores_json.get("score")) is not int:
            raise TypeError("Invalid JSON response: 'score' value is not an int")

        return scores_json

    def health_check(self):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Say this is a test!"}],
        )
        return completion.choices[0].message.content
