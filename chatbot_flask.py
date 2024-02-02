from flask import Flask, request, render_template
import openai
from langchain.chains import OpenAIChain

# Flask 애플리케이션 초기화
app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = 'YOUR_OPENAI_API_KEY'

# LangChain을 사용하여 OpenAI 챗봇 체인을 초기화 (예시로 OpenAIChain 사용, 실제 사용법은 LangChain 문서 참조)
chat_chain = OpenAIChain(api_key='YOUR_OPENAI_API_KEY')

@app.route('/')
def home():
    # 챗봇 UI를 포함한 메인 페이지를 렌더링
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']
    
    # OpenAI를 직접 사용하는 경우
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=user_message,
      temperature=0.7,
      max_tokens=150,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    openai_answer = response.choices[0].text.strip()

    # 또는 LangChain을 사용하는 경우
    # langchain_response = chat_chain.run(user_message)
    # langchain_answer = langchain_response['choices'][0]['message']['content']

    # 여기서는 OpenAI의 응답을 사용
    return {'answer': openai_answer}

if __name__ == '__main__':
    app.run(debug=True)
