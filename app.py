from flask import Flask, request, render_template
from PIL import Image
from encode_decode import *
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('encode.html')


@app.route('/encode', methods=['post', 'get'])
def encode():
    if request.method == 'POST':
        encode_img = request.files['encode_img']
        data_encode = request.form['data_encode']
        encode_img_name = request.form['encode_img_name']
        image = Image.open(encode_img)
        image.save('images/encode.png')
        steganography_encode(data_encode, encode_img_name)
        return render_template('decode.html')


@app.route('/decode', methods=['post', 'get'])
def decode():
    if request.method == 'POST':
        encode_img_name = request.form['decode_img_name']
        text = steganography_decode(encode_img_name)
        os.remove(encode_img_name)
        return '<p>Decoded message: <h1>{}</h1><p>'.format(text)


if __name__ == "__main__":
    app.run(debug=True)
