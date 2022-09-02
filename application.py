from flask import Flask
app = Flask(__name__)

# 일반적인 라우트 방식입니다.
@app.route('/')
def hello():
    return "<h3>Hello Helsinki!</h3>"

app.run(host="localhost",port=7777)