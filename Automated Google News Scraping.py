'''
【Google News】Automated Google News Scraping with Python: 
"Correlating with Stock Price Analysis for Investment Opportunities"
'''

#pip install GoogleNews first

from GoogleNews import GoogleNews

def main():
    # Initial Setups for Google News
    googlenews = GoogleNews()
    googlenews.setlang(lang='zh-TW')
    googlenews.setperiod('d')

    #Please type the Keyword of the news
    keyword = input("Please type the Keyword: ")
    googlenews.search(keyword)

    # Get Results
    result = googlenews.result()

    # Display the title of the news and links
    for item in result:
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        print('---')

if __name__ == "__main__":
    main()