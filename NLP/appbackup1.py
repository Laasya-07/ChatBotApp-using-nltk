import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

openai.api_key = 'sk-proj-hwFR1qZrNdxFbUrUHyuCT3BlbkFJabn4ZwN902aNJLF9r11g'


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/api')
def api():
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message
    else :
        return 'Failed to Generate response!'

if __name__ == '__main__':
    app.run(debug=True)
