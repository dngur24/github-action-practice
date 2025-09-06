from flask import Flask, render_template

app = Flask(__name__)

# 루트 URL에 대한 라우트
@app.route('/')
def index():
    # 'index.html' 템플릿을 렌더링하고 'name' 변수를 전달합니다.
    return render_template('index.html', name='Gemini')

if __name__ == '__main__':
    app.run(debug=True)