import re
import numpy as np

all_words = []
n = -1
with open("sentences.txt", 'r') as data_raw:
    for line in data_raw:
        a = re.split("[^a-z]", line.lower())
        somelist = [i for j, i in enumerate(a) if i != '']
        n += 1
        for i in somelist:
            all_words.append(i) 

dict_words = {}
index = 0
for i in all_words:
    if i not in dict_words:
        dict_words[i] = index
        index += 1

m = max(dict_words.values())
data = np.zeros((n + 1, m + 1))

n = -1
with open("sentences.txt", 'r') as data_raw:
    for line in data_raw:
        a = re.split("[^a-z]", line.lower())
        somelist = [i for j, i in enumerate(a) if i != '']
        n += 1
        for word in somelist:
            if word in dict_words:
                data[n, dict_words[word]] += 1

print results_cosine

results_cosine = []
for i in range(1, n + 1):
    results_cosine.append(scipy.spatial.distance.cosine(data[0,], data[i,]))
    
result = []
results_cosine_backup = list(results_cosine)
for i in range(2):
    result.append(min(results_cosine_backup))
    results_cosine_backup.remove(min(results_cosine_backup))

result_index = []
for i in range(2):
    result_index.append(results_cosine.index(result[i])+1)
result_index.sort()

f = open("result.txt", "a")
for i in result_index:
    f.write(str(i)+" ")

with open("result.txt", "r") as fil:
    for line in fil:
        print line