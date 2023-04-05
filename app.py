import subprocess
import platform

from flask import Flask, render_template,request

app = Flask(__name__)
#model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/result",methods=['POST'])
def result():
    user_input = request.form["user_input"]
    result = ""
    if platform.system() == "Windows":
    	result = subprocess.run(['python','result.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    else:
    	result = subprocess.run(['python3','result.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    new_result = result.stdout.decode().strip()

    data = eval(new_result)

    return render_template("index.html",result = data)




if __name__ == "__main__":
    app.run()

