import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
def tokenize_text(text):
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    return words
def extract_info(tokenized_words):
    num_wells = 0
    protein_ladder = False
    samples = []
    expected_bands = []

    for sentence in tokenized_words:
        for i, word in enumerate(sentence):
            if word.isdigit():
                num = int(word)

                if "well" in sentence[i - 1:i + 2]:
                    num_wells = num
                elif "sample" in sentence[i - 1:i + 2]:
                    samples.append(num)
                elif "band" in sentence[i - 1:i + 2]:
                    expected_bands.append(num)

            elif "PageRuler" in word:
                protein_ladder = True

    return num_wells, protein_ladder, samples, expected_bands
def parse_text(text):
    tokenized_words = tokenize_text(text)
    return extract_info(tokenized_words)
