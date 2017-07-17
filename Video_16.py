# https://www.youtube.com/watch?v=n3RqsMz3-0A

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7] # Can see quite easily this belongs to 'r'

# for i in dataset:
# 	for ii in dataset[i]:
# 		plt.scatter(ii[0],ii[1], s=100, color=i) # That's why dataset uses r and k lol

# This is the same as the code above, just 1 liner
# [[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0],new_features[1], s=100)
# plt.show()

def k_nearest_neighbors(data, predict, k=3):
	if len(data) >= k:
		warnings.warn('K is set to a value less than total voting groups!')

	# knnalgos
	return vote_result
