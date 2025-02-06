from flask import Flask, jsonify
from flask_cors import CORS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
CORS(app)

@app.route('/result')
def result():
    return jsonify({"message": "Hello world!"})

# template = """
# You are a game show host. Create a simple trivia question and give it four answer options (a, b, c, d).
# There are 10 questions in total. If the user answers incorrectly even once, the game is over. 
# Provide the question in the following format:

# a) [option]
# b) [option]
# c) [option]
# d) [option]

# Correct answer is: [a/b/c/d]

# The user has one chance to answer the question. 
# If the user answers incorrectly, you need to say: "Incorrect answer. The correct answer is: [a/b/c/d]. Game over." And then end the conversation.
# If the user answers correctly, you need to say: "Correct answer, lets move on to the next question." And then ask the next question.
# Do not ask the same question twice.
# Do not give the correct answer straight away.

# # History: {context}
# The user's previous answer: {answer}
# """

template = """

Answer the question below.

Here is the history of the conversation: {context}

Question: {question}

Answer:

"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_question():
    context = ""
    print("Welcome to the AI-chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": "", "question": user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    print("\nSovellus käynnistyy...")
    handle_question()
    app.run(debug=True)

