tweets_trump = Tweets(filtered_tweets_trump)
trump_voc_words = tweets_trump.filter_voc_words(method='lemmatization')

tweets_clinton = Tweets(filtered_tweets_clinton)
clinton_voc_words = tweets_clinton.filter_voc_words(method='lemmatization')

wordcloud_trump = " ".join(trump_voc_words)
wordcloud_clinton = " ".join(clinton_voc_words)

# Plot the wordclouds.
from PIL import Image
from wordcloud import WordCloud

def rep_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (0, random.randint(10, 100), random.randint(40, 60))

def dem_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(%d, %d%%, %d%%)" % (224, random.randint(40, 100), random.randint(40, 60))

pfont = {'fontname': 'Palatino Linotype'}
fig, ax = plt.subplots(1, 2, figsize=(10,6))

# masks taken from here:
# https://image.freepik.com/free-icon/elephant-republican-symbol_318-64492.jpg
# https://www.carstickers.com/prodimages/12960-democrat-donkey-sticker.png
republican_mask = np.array(Image.open(root_dir+'/figs/republican-symbol.jpg'))
democrat_mask = np.array(Image.open(root_dir+'/figs/democrat-symbol.jpg'))

wcloud_trump = WordCloud(background_color="white", 
                         max_words=200, 
                         mask=republican_mask, width=5000, height=5000)
wcloud_trump.generate(wordcloud_trump)
wcloud_trump.recolor(random_state=5, color_func=rep_color_func)

wcloud_clinton = WordCloud(background_color="white", 
                           max_words=200, 
                           mask=democrat_mask, width=5000, height=5000)
wcloud_clinton.generate(wordcloud_clinton)
wcloud_clinton.recolor(random_state=5, color_func=dem_color_func)

ax[0].set_title("Trump's Tweets", loc='left', fontsize=14, **pfont)
ax[0].imshow(wcloud_trump)
ax[0].axis('off')

ax[1].set_title("Clinton's Tweets", loc='left', fontsize=14, **pfont)
ax[1].imshow(wcloud_clinton)
ax[1].axis('off')
plt.show()

fig.savefig(root_dir + '/figs/pyladies_wordclouds_twitter.png', dpi=400)
