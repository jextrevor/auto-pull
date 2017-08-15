import subprocess
from bottle import run, post, request, response, get, route
@route("/pull",method="POST")
def process(path):
    process = subprocess.Popen(["git","pull"], cwd="/var/www/html")
    process.wait()
    return "Success"
run(host="localhost",port=8001)