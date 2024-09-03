import asyncio
from twikit import Client, TooManyRequests
from configparser import ConfigParser
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key='sk-9I2WMDsaLSNSrJVcNveS9ODCpp-WycDHsn4svkbedDT3BlbkFJgp04Qq_jBkCD4h3Pwlgzlt045Reh37EMZO0OOPsbUA')


  # Replace 

MINIMUM_TWEETS = 100
Query = 'India "India" (Earthquake OR Floods OR Landslide) -Bangladesh until:2024-08-24 since:2024-08-21'

config = ConfigParser()
config.read('config.ini')
username = config['X']['username']
email = config['X']['email']
password = config['X']['password']
client = Client(language='en-US')

def categorize_tweet(tweet_text):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are an assistant that categorizes tweets into one of the following categories: Flood, Earthquake, Landslide, Others."
        },
        {
            "role": "user",
            "content": f"Classify the following tweet into one of the categories(Please give a one word output): Flood, Earthquake, Landslide, Others.\nTweet: {tweet_text}\nCategory:"
        }
    ])
    category = response.choices[0].message.content.strip()
    return category



async def main():
    client = Client(language='en-US')



    client.load_cookies('cookies.json')

    tweet_count = 0
    tweet_list = []

    tweets = await client.search_tweet(Query, product='Top')

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


    df = pd.DataFrame(tweet_list, columns=['Tweet Number', 'Username', 'Tweet', 'Created At', 'Retweet Count', 'Favorite Count'])

    df['Category'] = df['Tweet'].apply(categorize_tweet)


    df.to_csv('categorized_tweets.csv', index=False)


if __name__ == '__main__':
    asyncio.run(main())