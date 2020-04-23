# 测试异步处理
from flask import Flask
import time
 
app = Flask(__name__)
 
@app.route('/')
def index():
    time.sleep(3)
    return 'Hello!'
 
if __name__ == '__main__':
    app.run(threaded=True)