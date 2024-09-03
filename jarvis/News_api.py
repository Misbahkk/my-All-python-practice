# import newsapi


# def get_pakistani_news_headlines():
#     """Gets Pakistani news headlines from NewsAPI."""
#     api = newsapi(api_key="5490dd781fae4accabe00d13ef05a715")
#     response = api.get_top_headlines(q="pakistan", country="pk")
#     headlines = []
#     for article in response["articles"]:
#         headlines.append(article["title"])
#     return headlines


# headlines = get_pakistani_news_headlines()
# for headline in headlines:
#     print(headline)


# ----------------------------------------------
''''
import requests
import pyttsx3


def get_pakistani_news_headlines():
    # Replace 'YOUR_API_KEY' and 'YOUR_NEWS_API_URL' with the actual API key and URL.
    api_key = '5490dd781fae4accabe00d13ef05a715'
    news_api_url = 'https://newsapi.org/v2/top-headlines?country=pk&category=business&apiKey=5490dd781fae4accabe00d13ef05a715'

    try:
        # Make a request to the news API to fetch headlines.
        response = requests.get(news_api_url, params={
                                'country': 'pk', 'apiKey': api_key})
        data = response.json()

        # Extract headlines from the API response.
        headlines = [article['title'] for article in data['articles']]
        return headlines
    except Exception as e:
        print("Error fetching news headlines:", str(e))
        return []


# def speak_text(text):
#     # Initialize the text-to-speech engine.
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Adjust the speaking rate (optional).
#     engine.say(text)
#     engine.runAndWait()


def main():
    print("Jarvis: Hello! I can read out headlines of Pakistani news for you.")
    while True:
        user_input = input("You: ").lower()

        if 'news' in user_input:
            headlines = get_pakistani_news_headlines()
            if headlines:
                print("Jarvis: Here are the latest headlines from Pakistani news:")
                for idx, headline in enumerate(headlines, 1):
                    print(f"{idx}. {headline}")
                    # Uncomment the line below to have Jarvis read out the headlines.
                    # speak_text(headline)
            else:
                print("Jarvis: Sorry, I couldn't fetch any headlines at the moment.")

        elif 'exit' in user_input or 'quit' in user_input:
            print("Jarvis: Goodbye!")
            break
        else:
            print("Jarvis: I'm sorry, I didn't understand. Please try again.")


if __name__ == "__main__":
    main()
'''


import requests


def get_pakistani_news_headlines():
    # Replace 'YOUR_API_KEY' and 'YOUR_NEWS_API_URL' with the actual API key and URL.
    #api_key = '5490dd781fae4accabe00d13ef05a715'
    news_api_url = 'https://newsapi.org/v2/top-headlines?country=pk&category=business&apiKey=5490dd781fae4accabe00d13ef05a715'

    try:
        # Make a request to the news API to fetch headlines.
        response = requests.get(news_api_url, params={
                                'country': 'pk', 'apiKey': api_key})
        data = response.json()

        # Extract headlines from the API response.
        headlines = [article['title'] for article in data['articles']]
        return headlines
    except:
        return []


# Get headlines
headlines = get_pakistani_news_headlines()
if headlines:
    print("Here are the latest headlines from Pakistani news:")
    for idx, headline in enumerate(headlines, 1):
        print(f"{idx}. {headline}")
else:
    print("Sorry, couldn't fetch any headlines at the moment.")
