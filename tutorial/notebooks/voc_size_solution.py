# Vocabulary depends on the number of tweets. For one person, more 
# tweets will normally mean more unique words, but also more word 
# repetitions. However, vocabulary size and word repetitions don't
# grow proportionally to the number of tweets, so it would be 
# incorrect to compare the two candidates by normalizing their 
# vocabulary measurements by the number of downloaded tweets. 
#
# Instead, we base our measurements on a fixed number of tweets, 
# which is chosen to be lower than both candidates number of tweets.
# Below, I've chosen 2500 tweets. The code selects 2500 random tweets 
# of each candidate, and calculates the number of unique words and 
# the average number of times a word is repeated. The code is run 
# several times, and the results are averaged in the end.
#
# Below, I suggest setting the number of repetitions (n_repeat) to 
# 5 or less, because the code takes a while to run. On my Mac, it's 
# about 1 min per iteration.

import random

n_repeat = 5
based_on_n_tweets = 2500

n_tweets_trump = filtered_tweets_trump.shape[0]
n_tweets_clinton = filtered_tweets_clinton.shape[0]

if based_on_n_tweets > min(n_tweets_trump, n_tweets_clinton):
    raise ValueError("""Number of tweets used for comparison should be smaller than either 
                        candidate's number of tweets.""")

voc_diversity_clinton = []
voc_diversity_trump = []

word_reps_clinton = []
word_reps_trump = []
    
for rep in range(n_repeat):
    choice_idx_trump = random.sample(range(n_tweets_trump), 
                                     based_on_n_tweets)
    choice_idx_clinton = random.sample(range(n_tweets_clinton), 
                                       based_on_n_tweets)

    tweets_trump = Tweets(filtered_tweets_trump.loc[choice_idx_trump,:])
    trump_voc_words = tweets_trump.filter_voc_words(method='stemming')
    trump_unique_words = tweets_trump.filter_unique_voc_words(method='stemming')

    tweets_clinton = Tweets(filtered_tweets_clinton.loc[choice_idx_clinton,:])
    clinton_voc_words = tweets_clinton.filter_voc_words(method='stemming')
    clinton_unique_words = tweets_clinton.filter_unique_voc_words(method='stemming')

    voc_diversity_trump.append(len(trump_unique_words))
    voc_diversity_clinton.append(len(clinton_unique_words))
    
    word_reps_clinton.append( len(clinton_voc_words) / len(clinton_unique_words) )
    word_reps_trump.append( len(trump_voc_words) / len(trump_unique_words) )

word_reps = {'clinton': np.mean(word_reps_clinton),
             'trump': np.mean(word_reps_trump)}
voc_diversity = {'clinton': np.mean(voc_diversity_clinton),
                 'trump': np.mean(voc_diversity_trump)}


# Make a nice bar plot.
plt.rcParams.update({'font.size': 14})
pfont = {'fontname': 'Palatino Linotype'}

plt.style.use('bmh')
fig, ax = plt.subplots(1, 2, figsize=(13,6))

bar_pos = [0.31, 0.69]
bar_width = 0.2

ax[0].bar(bar_pos, [word_reps['trump'], word_reps['clinton']], width=0.2, color=['firebrick', 'navy'])
ax[0].set_xticks([pos + bar_width/2 for pos in bar_pos])
ax[0].set_xticklabels(["DONALD TRUMP", "HILLARY CLINTON"], **pfont)
ax[0].set_title("Twitter vocabulary analysis based on posts between Dec 2015 and Aug 2016", 
                loc='left', y=1.02, fontsize=18, weight='bold', **pfont)
ax[0].set_ylabel('Average Word Repetitions', **pfont)
ax[0].set_ylim([1.05,7.95])
ax[0].set_xlim([0.2,1.0])

ax[1].bar(bar_pos, [voc_diversity['trump'], voc_diversity['clinton']], width=0.2, color=['firebrick', 'navy'])
ax[1].set_xticks([pos + bar_width/2 for pos in bar_pos])
ax[1].set_xticklabels(["DONALD TRUMP", "HILLARY CLINTON"], **pfont)
ax[1].set_ylabel('Vocabulary Size Based on 2500 Tweets', **pfont)
ax[1].set_ylim([550,2750])
ax[1].set_xlim([0.2,1.0])
fig.subplots_adjust(wspace=0.4)

fig.text(.21, .02, "'I know words, I have the best words.' — Donald Trump (Dec 30, 2015)", 
         style='oblique', weight='bold', fontsize=18, **pfont)

fig.savefig(root_dir + 'figs/pyladies_trump_vs_clinton_vocabulary.pdf')
