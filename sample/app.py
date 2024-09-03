from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Sample DataFrames for demonstration


@app.route('/tweets', methods=['GET'])
def api_tweets():
    data = [
        {'Tweet Number': 1, 'Username': 'User1', 'Tweet': 'Floods are affecting many regions.', 'Created At': '2024-08-21', 'Retweet Count': 120, 'Favorite Count': 45, 'Category': 'Flood', 'Location': 'Mumbai'},
        {'Tweet Number': 2, 'Username': 'User2', 'Tweet': 'Landslide reported in Himachal Pradesh.', 'Created At': '2024-08-22', 'Retweet Count': 80, 'Favorite Count': 30, 'Category': 'Landslide', 'Location': 'Shimla'}
    ]
    return jsonify(data)

@app.route('/news', methods=['GET'])
def api_news():
    data = [
        {'Source': 'Source1', 'Title': 'Heavy floods in Mumbai', 'Description': 'Mumbai is experiencing severe flooding.', 'Published At': '2024-08-21', 'URL': 'http://example.com/floods-mumbai', 'Category': 'Flood', 'Location': 'Mumbai'},
        {'Source': 'Source2', 'Title': 'Landslide in Himachal Pradesh', 'Description': 'A landslide has caused significant damage in Himachal Pradesh.', 'Published At': '2024-08-22', 'URL': 'http://example.com/landslide-himachal', 'Category': 'Landslide', 'Location': 'Shimla'}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
