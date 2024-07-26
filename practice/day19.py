# Day 19: 30 Days of python programming

from functools import reduce

def count_lines(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        text = reduce(lambda x, y: x + y, [len(line.split()) for line in lines])
        return (len(lines), text)
root = "/mnt/c/Users/mzhan/Desktop/30-Days-Of-Python/data"
f1 = root + "/obama_speech.txt"
print("Lines: {}\nWords: {}".format(*count_lines(f1)))

f2 = root + "/michelle_obama_speech.txt"
print("Lines: {}\nWords: {}".format(*count_lines(f2)))

f3 = root + "/donald_speech.txt"
print("Lines: {}\nWords: {}".format(*count_lines(f3)))

f4 = root + "/melina_trump_speech.txt"
print("Lines: {}\nWords: {}".format(*count_lines(f4)))

import json

def most_spoken_language(filename, num):
    with open(filename) as f:
        languages = {}
        string = f.read()
        countries = json.loads(string)
        for i in countries:
            for j in i["languages"]:
                if j in languages.keys():
                    languages[j] += 1
                else:
                    languages[j] = 1
        return [(v, k) for k, v in sorted(languages.items(), key = lambda x: x[1], reverse = True)][:num]
file = root + "/countries_data.json"
print(most_spoken_language(file, 10))
print(most_spoken_language(file, 3))

def most_populated_countries(filename, num):
    with open(filename) as f:
        population = {}
        string = f.read()
        countries = json.loads(string)
        for i in countries:
            population[i["name"]] = i["population"]
        return [{"countries":k, "population":v} for k, v in sorted(population.items(), key = lambda x: x[1], reverse = True)][:num]
file = root + "/countries_data.json"
print(most_populated_countries(file, 10))
print(most_populated_countries(file, 3))

file = root + "/email_exchanges_big.txt"
with open(file) as f:
    f.readlines()

import re

def find_most_common_words(filename, num):
    with open(filename) as f:
        occurances = []
        string = f.read()
        string = re.sub(r'[\[\]:;,."\n—-]', " ", string)
        words = re.split(r"[ ]+", string)
        while len(words) != 0:
            if words[0] == "":
                words.remove("")
            else:
                word = words[0]
                occurance = 0
                while word in words:
                    words.remove(word)
                    occurance += 1
                occurances.append((occurance, word))
        occurances.sort(key = lambda x: (x[0], x[1]), reverse = True)
        return occurances[:num]

print(find_most_common_words(f1, 10))

print(find_most_common_words(f2, 10))

print(find_most_common_words(f3, 10))

print(find_most_common_words(f4, 10))

def clean_text(text):
    text = re.sub(r'[\[\]:;,."\n—-]', " ", text)
    text = re.sub(r"\d+", "", text)
    return re.sub(r"\s+", " ", text).strip()

def check_similarity(filename1, filename2):
    strings1 = ""
    strings2 = ""
    with open(filename1) as f1:
        strings1 = f1.read()
    with open(filename2) as f2:
        strings2 = f2.read()
    strings1 = clean_text(strings1)
    strings2 = clean_text(strings2)
    words1 = strings1.split()
    words2 = strings2.split()
    similar = 0
    different = 0
    for i in words1:
        if i in words2:
            similar += 1
            words2.remove(i)
        else:
            different += 1
    return (similar / (similar + different + len(words2))) * 100

sim_score = check_similarity(f2, f4)
print("Michelle's and Melina's speeches have a similarity rating of {:.2f}%".format(sim_score))

file = root + "/romeo_and_juliet.txt"
print(find_most_common_words(file, 10))

file = root + "/hacker_news.csv"
with open(file) as f:
    strings = f.readlines()
    count1 = 0
    count2 = 0
    count3 = 0
    for i in strings:
        if bool(re.findall(r"[Pp]ython", i)):
            count1 += 1
        if bool(re.findall(r"[Jj]ava[Ss]cript", i)):
            count2 += 1
        elif bool(re.findall("Java", i)):
            count3 += 1
    print("{} lines include python or Python".format(count1))
    print("{} lines include javascript, Javascript, or JavaScript".format(count2))
    print("{} lines include Java and not JavaScript".format(count3))