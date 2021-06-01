import tweepy
import logging
import os

logging.basicConfig(level=logging.INFO,filename='config.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()


def create_api():
    # Authenticate to Twitter
	
	# Your Twitter Developer Labs App Consumer Key
    consumer_key = os.getenv("CONSUMER_KEY")
	
	# Your Twitter Developer Labs App Consumer Secret Key
    consumer_secret = os.getenv("CONSUMER_SECRET")

	# Your Twitter Developer Labs App Access Token
    access_token = os.getenv("ACCESS_TOKEN")
	
	# Your Twitter Developer Labs App Access Token Secret
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    logger.info("Creating OAuth Credentials for Twitter Authentication")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("Authentication OK!")
    return api