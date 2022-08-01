from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "1. Starting machine learning project. /n 2. ci/cd pipeline deployed."

if __name__ == "__main__":
    app.run(debug=True)

