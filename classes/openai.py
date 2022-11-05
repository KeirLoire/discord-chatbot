import json
import openai

class Model():
    def set_api_key(api_key):
        openai.api_key = api_key

    def submit_query(message):
        response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=f'User: {message.content}\nBot: ',
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
            best_of=1
        )

        if response['choices'][0]['text']:
            try:
                task = json.loads(response['choices'][0]['text'].lstrip())
                return task
            except Exception:
                return response['choices'][0]['text'].lstrip()

        else:
            return 'No response from OpenAI server.'