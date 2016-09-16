This is a comparative analysis of [Hillary Clinton's](https://twitter.com/HillaryClinton) and [Donald Trump's](https://twitter.com/realDonaldTrump) tweets. The repo contains the code and a couple of images used for the data visualization. Twitter's policy agreement does not allow me to share the data. If running the analysis, the code expects to read your Twitter API keys from a YAML file. Then the keys are used to download Twitter data using `tweepy`. The API only allows one to download a user's last 3200 tweets. Therefore, your results might be a little different than mine.

Running this analysis requires Python 3 and the following packages:

* yaml
* numpy
* matplotlib
* pandas
* tweepy
* bokeh

Downloading the data requires a Twitter account and API keys that one can generate here: https://apps.twitter.com/app/new
You must have a phone number associated with your Twitter account. This can be added in `Profile and settings -> Settings -> Mobile`: https://twitter.com/settings/add_phone?edit_phone=true
