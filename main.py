import os
import tweepy

from pprint import pprint

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

def init(print_tokens: bool = True) -> None:
    if print_tokens:
        print(f'Consumer Key: {consumer_key}')
        print(f'Consumer Secret: {consumer_secret}')
        print(f'Access Token: {access_token}')
        print(f'Access Token Secret: {access_token_secret}')
    
    if not consumer_key or not consumer_secret or not access_token or not access_token_secret:
        raise Exception('Please set the environment variables for the Twitter API keys')

def authenticate(api: tweepy.API) -> None:
    try:
        api.verify_credentials()
        print('Authentication successful')
    except:
        print('Authentication failed')
        exit(1)

def get_api(check_auth: bool = False) -> tweepy.API:
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    
    if check_auth:
        authenticate(api)
    return api

def get_my_posts(api: tweepy.API, count: int = 10) -> None:
    posts = api.user_timeline(count=count)
    pprint(posts)
    # for post in posts:
    #     print(post.text)
    
def get_liked_posts(api: tweepy.API, count: int = 10) -> None:
    posts = api.favorites(count=count)
    pprint(posts)
    # for post in posts:
    #     print(post.text)
    

if __name__ == '__main__':
    init(print_tokens=True)
    twitter_api = get_api(check_auth=True)
    
    twitter_api.destroy_status('1367923553102872582')
    # get_my_posts(twitter_api, 1)
    # get_liked_posts(twitter_api, 1)
    
    
    