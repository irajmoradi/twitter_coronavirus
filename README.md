# Map Reduce Class Project

This was a project for my Data Structures class at Claremont McKenna College. This project involved analysis of millions of tweets using MapReduce techniques. Utilizing both Shell scripts and Python code I parsed through all geotagged tweets in 2020, and created figures about the country and language for tweets containing certain hashtags related to the Coronavirus of 2020.


## Procedure 

Four Python programs were utilized in this data analysis. `map.py` looks through all files passed into it, which for the project being all geotagged tweets in 2020, searchs for hashtags, then calculates the origin country and language of the tweets with the hashtags.
`reduce.py` takes multiple files, the output files of `map.py`, and combines them into one file. `visualize.py` then charts the amount of tweets with a given hashtag by country or language, using the file produced by `reduce.py`. 
These three programs generated the four following figures:
 
Figure 1: # of Tweets in 2020 with the hashtag #코로나바이러스 by country of origin
<img src=Country%23코로나바이러스.png width=100% />
<br/><br/>
Figure 2: # of Tweets in 2020 with the hashtag #코로나바이러스 by language of origin
<img src=Language%23코로나바이러스.png width=100% />
<br/><br/>
Figure 3: # of Tweets in 2020 with the hashtag #coronavirus by country of origin
<img src=Country%23coronavirus.png width=100% />
<br/><br/>
Figure 4: # of Tweets in 2020 with the hashtag #coronavirus by language of origin
<img src=Language%23coronavirus.png width=100% />
<br/><br/>

The fourth program `alternative_reduce.py` takes all the files produced by map.py, and creates the following line chart using similar code to `reduce.py` and `visualize.py`. 
<img src=hi.png width=100% />
