from flask import Flask, make_response, jsonify

app = Flask(__name__)

# Register blueprints
from app.background import bp as background_bp
app.register_blueprint(background_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome to remove background service.'
    
    
@app.route('/health', methods=['GET'])
def health():
    return make_response(jsonify({"status": "Ok"}), 200)
  
  
if __name__ == '__main__':
    app.run()
