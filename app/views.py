from flask import Blueprint, render_template, request
import openai # type: ignore

openai.api_key = 'sk-proj-lwlUqz2BALqvwWgDoba0T3BlbkFJdgs413tnokiTGrqTBX9q'

views = Blueprint('views', __name__)

@views.route('/')
def chat():
    return render_template("chat.html")

@views.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.form.get("message")
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
        return('Failed to generate response')
       