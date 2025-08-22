from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
# index.html 파일을 실행시키기 위한 별도의 python 파일
