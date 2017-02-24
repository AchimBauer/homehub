from Flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Homehub Central'
  
if __name__ == '__main__':
  app.run(debug=True)
