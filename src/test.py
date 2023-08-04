import morss
import feedparser
import logging
import json
print(morss.__file__)
logging.getLogger().setLevel(logging.INFO)

url = 'https://feeds.bbci.co.uk/news/world/rss.xml'
# feed = feedparser.parse(url)
# logging.info("................................................")
# logging.info(feed)
# logging.info("................................................")

# options = morss.Options(format='rss')
# url,rss=morss.FeedFetch(url,options)
# rss = morss.FeedGather(rss, url, options)
# output = morss.FeedFormat(rss, options, 'unicode')
# morssFeed = feedparser.parse(output);
# logging.info(morssFeed)

xml_string = morss.process(url)
xml_string=feedparser.parse(xml_string)
logging.info(xml_string)