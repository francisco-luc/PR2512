# **Music Popularity Analysis: Identifying Patterns in Song Attributes**

Ignacio Palomares Martín  
Francisco Luc Aquaro

**INTRODUCTION**  
This dataset contains various popular songs with different attributes. These attributes can be categorized into more subjective measures (such as danceability or loudness) and more objective ones (like key or time signature). Additionally, we have the popularity of each song which, although somewhat subjective, is the central attribute of our dataset.

Since key and tempo are conceptually more straightforward to understand, we will primarily use these attributes along with popularity in our analysis. We will also explore other attributes such as danceability or speechiness, which may prove useful in certain contexts.

**DATA PREPROCESSING**  
For this dataset, we determined it would be valuable to include the release year of each song to identify patterns in how popularity correlates with publication year and various attributes.

Due to the large volume of data and the labor-intensive process of adding release years, we decided to reduce the dataset size, though we continue to gradually expand it. These modifications have resulted in a clean dataset without missing values, making it ready for analysis.

**RESEARCH OBJECTIVES AND METHODOLOGY**  
Our primary objective is to identify patterns among attributes that determine whether a song becomes popular. Additionally, we aim to investigate whether these patterns remain consistent across different time periods or how they evolve over the years.  
Initial Analysis Approach

1.  **Descriptive Statistics**: We will perform standard data processing on various attributes across the entire dataset and by time periods (calculating means, standard deviations, etc.) to establish our baseline understanding.  
     
2.  **Attribute Relationship Analysis**: We will explore combinations of attributes to identify if they follow known distributions. For example:  
     	 - Has the change in BPM (beats per minute) in songs been progressive over the years?
  		 - Is BPM distribution random across time periods?  
  		 - Do faster songs concentrate in specific years?

3.  **Clustering Analysis**: We will investigate whether our dataset can be meaningfully clustered into distinct groups. We'll test both K-means and hierarchical clustering algorithms to determine which produces better results, and experiment with different attribute combinations. For instance, we might visualize popularity differences between songs in A key versus C key.  
     
4.  **Classification Mode**l: Following the course's practical approach, we aim to develop a classifier that can predict whether a song should be popular based on its attributes.  
   

This comprehensive approach will allow us to uncover meaningful patterns in music popularity while accounting for changes in musical preferences over time.

**CHALLENGES**  
Our primary concern is the potential absence of clear patterns, which would complicate both clustering and classification efforts. Should this issue arise with the more objective attributes, we would shift our focus to exploring the subjective attributes instead.

Additionally, while our dataset includes songs from various eras, there is a significant imbalance between the number of recent songs and older ones. This disparity could hinder our pattern extraction process. If necessary, we may limit our analysis to songs from the 21st century, which still provides a substantial and interesting timeframe for analysis.

The uneven distribution across time periods might affect our ability to make reliable comparisons between different eras, potentially biasing our conclusions toward more recent musical trends. We'll need to account for this sampling bias in our interpretation of results or consider statistical approaches that can compensate for the imbalanced representation of different time periods.

**EXPECTED OUTCOMES**  
Through this analysis, we expect to discover several key insights:

1. **How Music Has Changed Over Time**: We hope to find out how musical preferences have shifted through the decades. Maybe the average tempo has gotten faster or slower, or certain keys have become more or less popular.

2. **What Makes Songs Popular**: We want to find specific attributes or combinations that consistently relate to higher popularity scores. This could show whether factors like danceability or energy matter more for a song's success than technical aspects like key or time signature.

3. **Natural Music Groupings**: Even though the dataset doesn't label genres, our clustering analysis might reveal natural groupings that match different musical styles, each with their own distinct attribute profiles.

4. **Prediction Accuracy**: We'll evaluate how well our classification model works to see if song popularity can actually be predicted from audio features alone. This will help us understand whether popularity comes from measurable audio characteristics or from other factors not in our dataset.  
