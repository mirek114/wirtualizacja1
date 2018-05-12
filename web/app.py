from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return "Dzila"

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)

@app.route("/order-animation")
def order_animation():
  return render_template(
    "order.html",
    invitation="siema"
  )

@app.route("/upload")
def upload():
  if 'my_file' not in request.files:
    return "nie pyklo"
  upl_file = request.files['my_file']
  storage = new S3Storage(os.get, s3)
  storage.save(path="", body=upl_file)
