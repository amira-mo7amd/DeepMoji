from __future__ import print_function, division, unicode_literals
import json
import numpy as np
from torchmoji.sentence_tokenizer import SentenceTokenizer
from torchmoji.model_def import torchmoji_emojis
from torchmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH
import sys

print("start the file")
message = sys.argv[1] + ""


def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]


maxlen = 30
print('Tokenizing using dictionary from {}'.format(VOCAB_PATH))
with open(VOCAB_PATH, 'r') as f:
    vocabulary = json.load(f)
st = SentenceTokenizer(vocabulary, maxlen)
model = torchmoji_emojis(PRETRAINED_PATH)
print(model)
tokenized, _, _ = st.tokenize_sentences([message])
prob = model(tokenized)
ind_top = top_elements(prob[0], 5)
print(ind_top)
