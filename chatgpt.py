import openai
import configparser
from flask import Flask, request

app = Flask(__name__)

@app.route('/ai', methods=['GET'])
def chatgpt():
    user, message = request.args.get('user'), request.args.get('message')
    ai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": example_in},
                {"role": "assistant", "content": example_response},
                {"role": "user", "content": f'{user}: {message}'},
            ]
        )['choices'][0]['message']['content']
    return ai_response[:350] + '...' if len(ai_response) > 350 else ai_response

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('/root/secret.cfg')
    openai.api_key = config['openai']['api-key']
    with open('/root/system_prompt.txt', 'r') as f: system_prompt = f.read()
    with open('/root/example_in.txt', 'r') as f: example_in = f.read()
    with open('/root/example_response.txt', 'r') as f: example_response = f.read()
    app.run('0.0.0.0', port=8080)