import numpy as np

scores, _, numTweets= np.loadtxt('newoutput.txt', dtype=str, skiprows=1, unpack=True)
scores = np.array(scores, dtype=int)
numTweets=np.array(numTweets, dtype=int)

totalTweets = np.sum(numTweets)

meanScore = np.sum(scores*numTweets)/totalTweets

print(meanScore)

