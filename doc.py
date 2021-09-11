import docx2txt
import pandas as pd
import numpy as np
import re
import tensorflow as tf
import cv2 as cv
import time
from tensorflow.keras.layers.experimental import preprocessing
import numpy as np
import os
import nltk
import stopwords
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize
nltk.download('punkt')
# read in word file

print("0_0 ....")
PATH = "C:/Users/User/Desktop/dataset/DataSet_MR"
for root, dirs, files in os.walk(PATH):
    for filename in files:
        path_file = (os.path.join(root, filename))
        if path_file.__contains__('~') or path_file.endswith('doc'):
            continue
        if path_file.__contains__('xml'):
            pass
        path_file = path_file.replace("/", "\\")
        print(path_file)
        result = docx2txt.process(path_file)
        res = nltk.word_tokenize(result.lower())
        stop_words = set(stopwords.words('russian'))

        filtered_sentence = [w for w in res if not w in stop_words]

        filtered_sentence = []

        for w in res:
            if w not in stop_words:
                filtered_sentence.append(w)

        # res.remove('.')
        # res.remove(',')

        print(filtered_sentence)
