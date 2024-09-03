import asyncio
from twikit import Client
from configparser import ConfigParser
import pandas as pd
import requests  # New import for News API
from openai import AsyncOpenAI
from datetime import datetime


openai_client = AsyncOpenAI(api_key='sk-9I2WMDsaLSNSrJVcNveS9ODCpp-WycDHsn4svkbedDT3BlbkFJgp04Qq_jBkCD4h3Pwlgzlt045Reh37EMZO0OOPsbUA')

MINIMUM_TWEETS = 100
Query = 'India "India" (Earthquake OR Floods OR Landslide OR Cyclone) -Bangladesh until:2024-08-24 since:2024-08-21'

config = ConfigParser()
config.read('config.ini')
username = config['X']['username']
email = config['X']['email']
password = config['X']['password']
twitter_client = Client(language='en-US')

NEWS_API_KEY = '219c89838353478891a3c1daa5f32872'  # Replace with your actual News API key
NEWS_QUERY = 'India AND (Earthquake OR Floods OR Landslide OR Cyclone)' 
NEWS_API_URL = f'https://newsapi.org/v2/everything?q={NEWS_QUERY}&apiKey={NEWS_API_KEY}'

async def categorize_tweet(tweet_text):
    try:
        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that categorizes tweets into one of the following categories: Flood, Earthquake, Landslide, Others."
                },
                {
                    "role": "user",
                    "content": f"Classify the following tweet into one of the categories (Please give a one-word output): Flood, Earthquake, Landslide, Others.\nTweet: {tweet_text}\nCategory:"
                }
            ]
        )
        # Extract the category from the response
        category = response.choices[0].message.content.strip()
        return category
    except Exception as e:
        print(f"Error categorizing tweet: {e}")
        return "Others"  # Default category in case of an error

async def categorize_location(tweet_text):
    try:
        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an assistant that analyzes tweets to identify the most likely city or location where an event occurred. "
                        "If the tweet mentions a recognizable city or location, extract it. "
                        "If the location is not clear, return 'Unknown'."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Analyze the following tweet to determine the location (city) where the event occurred.Please respond in only one word "
                        f"If the location is not mentioned or cannot be determined, please return 'Unknown'.\n\nTweet: {tweet_text}"
                    )
                }
            ]
        )
        # Extract the category from the response
        location = response.choices[0].message.content.strip()
        return location
    except Exception as e:
        print(f"Error categorizing tweet: {e}")
        return "Unknown2"  # Default category in case of an error

def fetch_news_articles():
    try:
        response = requests.get(NEWS_API_URL)
        response.raise_for_status()  # Check for request errors
        news_data = response.json()
        articles = news_data.get('articles', [])
        news_list = []

        for article in articles:
            news_data = [
                article['source']['name'],
                article['title'],
                article['description'],
                article['publishedAt'],
                article['url']
            ]
            news_list.append(news_data)

        return news_list
    except Exception as e:
        print(f"Error fetching news articles: {e}")
        return []

async def main():
    # twitter_client.load_cookies('cookies.json')

    tweet_count = 0
    tweet_list = []
    tweets=None
    MINIMUM_TWEETS=50
    while(tweet_count<MINIMUM_TWEETS):
    
    # Fetch tweets based on the query
        if tweets is None:
         print(f'{datetime.now()} - Getting tweets...')
         tweets = await twitter_client.search_tweet(Query, product='Top')
        else:
            print(f'{datetime.now()} - Getting tweets...')
            tweets=await tweets.next()
        # Process each tweet and collect data
        for tweet in tweets:
            tweet_count += 1
            tweet_data = [
                tweet_count,
                tweet.user.name,
                tweet.text,
                tweet.created_at,
                tweet.retweet_count,
                tweet.favorite_count
            ]
            tweet_list.append(tweet_data)

    # Create a DataFrame from the collected tweet data
    df_tweets = pd.DataFrame(tweet_list, columns=['Tweet Number', 'Username', 'Tweet', 'Created At', 'Retweet Count', 'Favorite Count'])

    # Apply the categorization function to the 'Tweet' column
    categories = await asyncio.gather(*[categorize_tweet(tweet) for tweet in df_tweets['Tweet']])
    df_tweets['Category'] = categories
    location = await asyncio.gather(*[categorize_location(tweet) for tweet in df_tweets['Tweet']])
    df_tweets['Location'] = location
    # Fetch news articles
    news_list = fetch_news_articles()

    # Create a DataFrame from the news data
    df_news = pd.DataFrame(news_list, columns=['Source', 'Title', 'Description', 'Published At', 'URL'])
    categories = await asyncio.gather(*[categorize_tweet(description) for description in df_news['Description']])
    df_news['Category'] = categories
    locations = await asyncio.gather(*[categorize_location(description) for description in df_news['Description']])
    df_news['Location'] = locations

    # Save the DataFrames to CSV files
    #df_tweets.to_csv('categorized_tweets.csv', index=False)
    #df_news.to_csv('news_articles.csv', index=False)
    
    #print("CSV files have been saved successfully.")


if __name__ == '__main__':
    asyncio.run(main())





