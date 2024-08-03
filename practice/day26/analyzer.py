import re
from functools import reduce

def clean(text):
    text = re.sub(r'[()\[\]:;,."\n—-]', " ", text)
    text = re.sub(r"\d+", "", text)
    return re.sub(r"\s+", " ", text).strip()

def concat(x, y):
    return x + y

def analyze(content):
    cleaned = clean(content)

    tokens = cleaned.split()

    words = len(tokens)

    chars = len(reduce(concat, tokens))

    frequency = []
    while len(tokens) != 0:
        occurance = re.findall(r"\b"+tokens[0]+r"\b", cleaned)
        frequency.append((tokens[0], len(occurance)))
        for i in occurance:
            tokens.remove(i)
    frequency.sort(key = lambda x: (x[1], x[0]), reverse = True)
    
    return (words, chars, frequency)