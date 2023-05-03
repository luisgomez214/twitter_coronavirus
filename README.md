# Coronavirus twitter analysis

Below is the geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.

**Learning Objectives:**

1. I worked with large scale datasets
1. I worked with multilingual text
1. I used the MapReduce divide-and-conquer paradigm to create parallel code

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
The lambda server's `/data/Twitter dataset` folder contains all geotagged tweets that were sent in 2020.
In total, there are about 1.1 billion tweets in this dataset.

The tweets are stored as follows.
The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`,
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format.
JSON is a popular format for storing data that is closely related to python dictionaries.

I completed the following tasks:

Task 0: Create the mapper

I modified the `map.py` file so that it tracks the usage of the hashtags on both a language and country level.

Task 1: Run the mapper

I created a shell script called `run_maps.sh`.
This file looped over each file in the dataset and ran the `map.py` command on that file.

Task 2: Reduce

After the modified `map.py` ran on all the files,
I had a large number of files in my `outputs` folder.
I used the `reduce.py` file to combine all of the `.lang` files into a single file,
and all of the `.country` files into a different file.

Task 3: Visualize

I modified the `visualize.py` file so that it generates a bar graph of the results and stores the bar graph as a png file.
The horizontal axis of the graph are the keys of the input file,
and the vertical axis of the graph are the values of the input file.
The final results are sorted from low to high, and you only include the top 10 keys.

#coronavirus Usage by Country in 2020
 
<img src=coronavirus_country.png  width=50% />

The bar graph above depicts the amount of times the word "coronavirus" was tweeted in 2020. The graph is sectioned by country, with the US being the leading country with the most tweets.

#coronavirus Usage by Language in 2020

<img src=coronavirus_lang.png  width=50% />

The bar graph above depicts the amount of times the word "coronavirus" was tweeted in 2020. The graph is sectioned by language, with the english being the leading language with the most tweets.

#코로나바이러 Usage by Country in 2020

<img src=코로나바이러스_country.png  width=50% />

The bar graph above depicts the amount of times the word "코로나바이러" was tweeted in 2020. The graph is sectioned by country, with the Korea being the leading country with the most tweets.

#코로나바이러 Usage by Language in 2020

<img src=코로나바이러스_lang.png  width=50% />

The bar graph above depicts the amount of times the word "코로나바이러" was tweeted in 2020. The graph is sectioned by language, with the korean being the leading language with the most tweets.

Task 4: Alternative Reduce

I created a new file 'alternative_reduce.py'. This file took as input on the command line a list of hashtags, and output a line plot where:

There is one line per input hashtag.
The x-axis is the day of the year.
The y-axis is the number of tweets that use that hashtag during the year.

I then plotted the data


<img src=myplot13.png  width=50% />

The line graph above depicts # of Tweets with a certain hashtag by each day in 2020. 
