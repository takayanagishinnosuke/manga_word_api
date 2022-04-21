import importlib
from flask import Flask , jsonify
from flask import request
from flask_cors import CORS
import word_dcdc

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def post():
  if request.method == 'GET':
    importlib.reload(word_dcdc)
    word = "「" + word_dcdc.origin_text + "」"

  return jsonify(word) #jsonで返す

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=888, debug=True)




# %%
