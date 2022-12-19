from ensure import ensure_annotations
from PYPIPackage.manual_exception import InvalidListException
from PYPIPackage.logger import logger
import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords  # remove stopwords
from nltk.stem.porter import PorterStemmer  # stemming
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
from nltk.stem import WordNetLemmatizer


@ensure_annotations
def text_preprocessing(main_list: list) -> list:
    try:
        corpus = []
        if main_list is None:
            raise InvalidListException("list cannot be null")
        elif type(main_list) is not list:
            raise InvalidListException("input should be in list format")
        else:
            lemmatizer = WordNetLemmatizer()
            for i in range(len(main_list)):
                review = re.sub('[^a-zA-Z]', ' ', main_list[i])
                logger.info(f"removing punctuations: {review}")
                review = review.lower()
                logger.info(f"lowering the sentence: {review}")
                review = review.split()
                review = [lemmatizer.lemmatize(word) for word in review if not word in stopwords.words('english')]
                logger.info(f"lemmatizing each words: {review}")
                review = ' '.join(review)
                corpus.append(review)
                logger.info(f"successfully preprocessed")
        return corpus
    except Exception as e:
        raise e

