import openai

openai.api_key = ''

def get_openai_response(text_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[              
                {"role": "user", "content": text_input}
            ],
            max_tokens=150  
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error getting OpenAI response: {e}")
        return None