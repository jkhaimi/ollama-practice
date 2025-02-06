from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
CORS(app)

template = """
Answer the question below.

Here is the history of the conversation: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_question = data.get("question", "")
    if not user_question:
        return jsonify({"error": "No question provided"}), 400
    
    result = chain.invoke({"context": "", "question": user_question})
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)
