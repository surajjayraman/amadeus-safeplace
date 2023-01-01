from flask import Flask
app = Flask(__name__)
@app.route('/')
def safeplace():
   return 'Safe Place'
if __name__ == '__main__':
   app.run()