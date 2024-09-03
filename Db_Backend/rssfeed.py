from flask import Flask, jsonify
import json
import feedparser
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# List of RSS feed URLs
RSS_FEEDS = [
    "https://timesofindia.indiatimes.com/rssfeeds/1221656.cms",
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "https://timesofindia.indiatimes.com/rssfeedmostrecent.cms",
    "https://www.thehindu.com/news/national/feeder/default.rss",
    "https://feeds.feedburner.com/ndtvnews-india-news",
    "https://www.news18.com/commonfeeds/v1/eng/rss/india.xml",
]

# Keywords to filter for disaster-related news
DISASTER_KEYWORDS = ["disaster", "earthquake", "flood", "cyclone", "hurricane", "tsunami", "landslide", "wildfire", "storm"]

# To store the links of already fetched news
fetched_news_links = set()

def fetch_disaster_news(feed_urls, keywords):
    """
    Fetch disaster-related news from multiple RSS feeds.

    Parameters:
    - feed_urls: A list of RSS feed URLs.
    - keywords: A list of keywords to filter news entries.

    Returns:
    - A list of new disaster-related news entries from the feeds.
    """
    new_disaster_news = []

    for feed_url in feed_urls:
        print(f"Fetching data from: {feed_url}")
        # Parse the RSS feed
        feed = feedparser.parse(feed_url)

        # Check for errors in fetching the feed
        if feed.bozo:
            print(f"Failed to fetch data from RSS feed. Error: {feed.bozo_exception}")
            continue

        # Extract and filter relevant news entries based on keywords
        for entry in feed.entries:
            title = entry.get("title", "").lower()
            description = entry.get("description", "").lower()
            link = entry.get("link", "")

            # Check if the entry has already been fetched
            if link in fetched_news_links:
                continue  # Skip already fetched entries

            # Check if any of the keywords are present in the title or description
            if any(keyword in title or keyword in description for keyword in keywords):
                news_info = {
                    "title": entry.get("title"),
                    "description": entry.get("description"),
                    "link": link,
                    "published": entry.get("published")
                }
                new_disaster_news.append(news_info)
                fetched_news_links.add(link)  # Add link to fetched news set

    return new_disaster_news

# Infinite loop to continuously check for new disaster news
while True:
    # Fetch new disaster news from the RSS feeds
    new_disaster_news = fetch_disaster_news(RSS_FEEDS, DISASTER_KEYWORDS)

    # Display fetched disaster news if there are new updates
    if new_disaster_news:
        # Arrange data in an array of objects
        disaster_news_objects = [
            {
                "title": news['title'],
                "description": news['description'],
                "link": news['link'],
                "published": news['published']
            } for news in new_disaster_news
        ]



    @app.route('/rssfeed', methods=['GET'])
    def get_disaster_news():
    # Return the array of objects as JSON
        return jsonify(disaster_news_objects)

    if __name__ == '__main__':
        app.run(debug=True)

    # # Wait for a specified interval before fetching the news again
    # time.sleep(10)  # Wait for 10 seconds






