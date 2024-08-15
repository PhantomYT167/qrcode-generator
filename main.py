from flask import Flask, render_template, request
import segno

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/home') 
def home():
    url = request.args.get('url') 
    qrcode = segno.make(url, micro=False)
    qrcode_path = 'static/qrcode.png' 
    qrcode.save(qrcode_path, scale=10) 
    return render_template('index.html', qrcode=qrcode_path)
@app.route('/')
def index():
    name = "Ismoil"
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
