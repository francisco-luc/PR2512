MUSIC DATA ANALYSIS
DATA MINING

Ignacio Palomares & Francisco Luc


INTRODUCTION

This reports present a detailed exploration of music features. We want to discover how musical characteristics have changed, what characteristics influence popularity and if songs can be grouped of popular predicted based in the features.

We have used a Kaggle dataset designed for machine learning for genre classification. We've changed the aim of the dataset, focusing on how popularity is related with the other music features.


DATASET OVERVIEW.

The dataset includes nearly one thousand songs with the following attributes.

- Artist name.

- Track name.

- Popularity.

- Danceability. How suitable is a track for dancing.

- Energy. Perceived intensity.

- Key. (Encoded with numbers). Musical tone of the song.

- Mode. (Encoded with 0 and 1). (Minor/Major)

- Loudness.

- Speechiness. Presence of spoken word.

- Acousticness. Acoustic songs.

- Liveness. Probability of the song to be recorded live.

- Valence. Musical Positivity.

- Tempo. Beats per minute.

- Duration. Length of the track

- Release Year.


DATA PREPROCESSING

We added manually another feature: release year. We thought it was needed to place temporally each song for understanding how popularity and the rest of the features works.

We've deleted manually the missing value but we also make some functions to handle missing values through median values for numerical features, and most frequent for categorical features.

Also we've changed the duration from milisecond to minutes, and we divided the songs through decades and through bigger eras for better understanding.

- Vintage Era (1927-1959)

- Classic Era (1960-1979)

- Modern Era (1980-1999) 

- Contemporary Era (2000 onwards).

Most of the songs are form the Contemporary and Modern Era.



DESCRIPTIVE ANALYSIS AND DATA DISTRIBUTION

The dataset includes song from 1927 to 2023, nearly one century of music. Most of the songs of the dataset are contemporary or the last part of the last century.

Popularity goes from 1 to 94, with a median of 45, which means a moreover equilibrated distribution, with less songs extremely popular than extremely unpopular.

Regarding the duration of the songs, most of the song's duration goes from 2 to 4 minutes, while we can find some atypical values like songs that lasts 10 minutes.

The tonalities of the song is pretty uneven, with certain frequent tonalities, showing some conventions or traditions.

The major mode (1) is more frequent than the minor (0). Major mode is related with positive sounds and minor mode with more 'sad' sounds. So seems normal that there are more positive or happy songs than sad.

images/distribution.png


TEMPORAL ANALYSIS

Music has evolved through the years, showing certain changes in audio features. This shows how the music production has changed in such a convulsing century.

Contemporary music seams to have more Danceability and Energy comparing to modern and moreover with the Classic era.

The songs seems to be more noisy with time, increasing the volume trough the years with a mean of 6dB.

Tempo (bpm) has changed through the decades with a small general change in the 2010 decade regarding other decades.

Acousticness has decreased a lot because the electronic production has established in the industry. It decreased form 0.6 in the '60 to 0.3 in the las decades.

Seems to be a positive correlation between the release year and the popularity, with seems accurate because of the streaming platforms.




OUTLIERS ANALYSIS

We've found meaningful atypical changes in the tempo (bpm) with songs that goes over the 200bpm while most of the songs goes from 90bpm to 130bpm.

We also found outliers in the duration of the songs, with extremely long songs, like songs with more of 10 min of duration. It make sense because genres like progressive rock or electronic make longer songs than pop or rock music. 

The popularity show not so much atypical values. As we said before, the median is almost in the center of the values, showing an equilibrated dataset. This means that the reception of the songs seems to be continue, with no many big failures of success.

Energy and acousticness showed also equilibrated distributions, which means that the production regarding this features seems more standarized.

The IQ range analysis showed that approximately the 10% of the songs could be atypical in one of the features.




CORRELATION ANALYSIS

Energy and Volume show a strong positive correlation (r = 0.7). This means that louder songs are perceived as more energetic.

In the other hand, acousticness has a strong negative correlation (r = 0.6). That confirms that acoustic songs are perceived as less energetics that electronic songs.

Danceabilty and Valence (music positivity) have a positive correlation, which means that danceable songs seems to be happy.

Tempo doesn't have strong correlations with any feature that means than changes a lot how it work with different songs.

Duration and popularity show a small negative correlation, that means that there is no big relationship or a perfect duration.




CLUSTERING ANALYSIS

We've identified 4 different clusters based in the audio features. We've used the elbow method for compute this value and later used K-mean for clustering.

Each cluster represents a different style with music with different popularities.

- Cluster 0. High energy songs (0.71), very danceable (0.67) and mid-high popularity (54.3). Could be related with rock or electronic music.

- Cluster 1. Mid tempo songs (108bpm), moderated energy (0.55) and medium popularity (approx 50). Can be pop music or soft rock.

- Cluster 2. Low energy songs (0.31), less danceable (0.45) and low popularity (38.1). Probably folk music or songwriters.

- Cluster 3. Speedy songs (132bpm), high energy (0.79) and high popularity (58.2). Also could be related with rock and electronic.


The hierarchical analysis approved the K-means approach, showing similar groups in PCA visualization.

The dendogram showed a clearly separation between the groups.





CLASSIFICATION ANALYSIS

Random Forest Algorithm showed the best precision (73%), over the decision trees (68) and Naive Bayes (64%)

The most important characteristic to predict the popularity were energy, volume and danceability.

The model is more reliable for identifying successfull songs than no popular songs.

Models show that we can predict in some point the popularty, but not all. There are another factors that also help a song to be popular, like fame or marketing.

The less predictive characteristics were acousticness and liveness. 



CONCLUSIONS

Music has become more energetic, louder, and electronic. This make sense because the accelerated society and the digital tools.

Danceability and valence captures the listener mood.

The clustering reflect different genres or moods.

Audio features can be a beginning for predict if a song can be popular, but there's a lot of other reasons why a song can be popular. 


 
