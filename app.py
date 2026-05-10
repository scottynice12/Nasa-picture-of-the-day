from flask import Flask, jsonify
import requests

app = Flask(__name__)

NASA_URL = "https://api.nasa.gov/planetary/apod"
DEMO_KEY = "DEMO_KEY"

@app.route('/apod')
def get_nasa_picture():
    response = requests.get(NASA_URL, params={'api_key': DEMO_KEY})
    data = response.json()
    return jsonify({
        'title': data['title'],
        'url': data['url']
    })

@app.route('/apod/image')
def get_apod_image():
    response = requests.get(NASA_URL, params={'api_key': DEMO_KEY})
    data = response.json()
    img_url = data['url']
    img_response = requests.get(img_url)
    return img_response.content, 200, {'Content-Type': 'image/jpeg'}

if __name__ == '__main__':
    app.run(debug=True)
