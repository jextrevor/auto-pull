import subprocess
from bottle import run, post, request, response, get, route
@route("/pull",method="POST")
def process():
    process = subprocess.Popen(["git","pull"], cwd="/var/www/html")
    process.wait()
    return "Success"
run(host="0.0.0.0",port=8001)