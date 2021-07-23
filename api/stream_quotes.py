### import
import logging
import yaml

with open('../yaml/url.yml') as u:
    urls = yaml.safe_load(u)

with open('../yaml/paper.yml') as p:
    paper = yaml.safe_load(p)

from alpaca_trade_api.stream import Stream


### async stuff
async def print_quote(q):
    print('quote', q)

### main
def main():
    feed = 'iex'  # <- replace to SIP if you have PRO subscription
    stream = Stream(paper.key, paper.secret, data_feed=feed, raw_data=True)
    stream.subscribe_quotes(print_quote, 'IBM')
    stream.run()


if __name__ == "__main__":
    # main()
