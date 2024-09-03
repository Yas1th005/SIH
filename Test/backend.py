from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/tweets')
def get_tweets():
    data = [
        {
            'disaster': 'Flood',
            'location': 'Mumbai',
            'description': 'Heavy rains have caused flooding in Mumbai.'
        },
        {
            'disaster': 'Earthquake',
            'location': 'Nepal',
            'description': 'A recent earthquake has caused significant damage in Nepal.'
        },
        {
            'disaster': 'Cyclone',
            'location': 'Bangladesh',
            'description': 'Cyclone has hit the coast of Bangladesh.'
        }
    ]
    return jsonify(data)

@app.route('/news')
def api_news():
    data = [
        {'Source': 'Source1', 'Title': 'Heavy floods in Mumbai', 'Description': 'Mumbai is experiencing severe flooding.', 'Published At': '2024-08-21', 'URL': 'http://example.com/floods-mumbai', 'Category': 'Flood', 'Location': 'Mumbai'},
        {'Source': 'Source2', 'Title': 'Landslide in Himachal Pradesh', 'Description': 'A landslide has caused significant damage in Himachal Pradesh.', 'Published At': '2024-08-22', 'URL': 'http://example.com/landslide-himachal', 'Category': 'Landslide', 'Location': 'Shimla'}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
