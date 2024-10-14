from flask import Flask,jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify("Le Python c'est bon mangez en")

@app.route('/color')
def hello_color():
    return jsonify("RedTeam")

@app.route('/whoami')
def get_tasks():
    ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
    return jsonify({'ip_hote': ipv4}), 200
@app.route('/env')
def getmonenv():
    environment_variables = { key: os.environ[key] for key in os.environ.keys() }
    return jsonify(**environment_variables)
 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
