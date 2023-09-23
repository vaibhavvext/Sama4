import requests
from twilio.rest import Client
import uagents 
from uagents import Agent, Context

Sama4 = Agent(
    name="Sama4",
    port=8000,
    seed="Sama4 secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)


# Twilio credentials
twilio_account_sid = "ACbbe5a2bb9ceb4e861a626745192c1aa1"
twilio_auth_token = "67def8847e9504491846835cf34d8144"
twilio_phone_number = "+13342342538"
recipient_phone_number = "+919099469577"

api_key = "14062f5950c34680bbdc56cab5bfad61"

def send_sms(message):
    # Initialize Twilio client
    client = Client(twilio_account_sid, twilio_auth_token)

    # Send SMS
    client.messages.create(
        to=recipient_phone_number,
        from_=twilio_phone_number,
        body=message
    )

def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + api_key
    news_data = requests.get(main_url).json()
    
    articles = news_data["articles"]
    
    news_articles = []
    for article in articles:
        news_articles.append(article['title'])

    # Limit the number of articles to 5
    news_articles = news_articles[:5]

    # Join the titles into a single string
    news_titles = "\n".join(news_articles)

    # Send the news titles as an SMS
    return(news_titles)

@Sama4.on_interval(period = 10.0)
async def agent(ctx:Context):
    agent = news()
    ctx.logger.info(agent)
    send_sms(agent)

if __name__ == "__main__":
    Sama4.run()