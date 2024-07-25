# Day 18: 30 Days of python programming

import re

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

words = re.split(r"[.]* |[.]", paragraph)
occurances = []
while len(words) != 0:
    if words[0] == "":
        words.remove("")
    else:
        occurance = re.findall(r"\b"+words[0]+r"\b", paragraph)
        occurances.append((len(occurance), words[0]))
        for i in occurance:
            words.remove(i)
occurances.sort(key = lambda x: (x[0], x[1]), reverse = True)
print(occurances)

string = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
points = re.findall(r"[-]*\d+", string)
sorted_points = sorted([int(x) for x in points])
distance = sorted_points[-1] - sorted_points[0]
print(distance)

def is_valid_variable(var):
    pattern = r"[A-Za-z_][A-Za-z0-9_]*$"
    return bool(re.match(pattern, var))
print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'
def clean_text(text):
    return re.sub(r"[%$@,&#;.!?]", "", text)
print(clean_text(sentence))
def most_frequent_words(text):
    words = re.split(r" ", text)
    occurances = []
    while len(words) != 0:
        occurance = re.findall(r"\b"+words[0]+r"\b", text)
        occurances.append((len(occurance), words[0]))
        for i in occurance:
            words.remove(i)
    occurances.sort(key = lambda x: (x[0], x[1]), reverse = True)
    return occurances[:3]
print(most_frequent_words(clean_text(sentence)))