from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/', methods=['POST'])
def feature_1():
  data = request.get_json()
  return jsonify({"input":data})
if __name__ == "__main__":
    app.run(debug=True)
