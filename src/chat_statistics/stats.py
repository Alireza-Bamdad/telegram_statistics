import json
from collections import Counter 
from hazm import word_tokenize, Normalizer
from wordcloud import WordCloud 
from bidi.algorithm import get_display
import matplotlib.pyplot as plt
from pathlib import Path




from src.data import DATA_DIR
class ChatStatistics:
    def __init__(self, chat_json):

        #load chatdata
        with open(chat_json) as f:
            self.chat_data = json.load(f)

        self.normalizer = Normalizer()

        #load stopwords
        stopword = open(str(Path(DATA_DIR / 'stopword.txt'))).readlines()
        self.stopword =list(map(str.strip, stopword))

    def geanarate_word_cloud(self, output_dir):
        """
        ganerate a word cloud from chat data
        
        """
        text_content = ''

        for msg in self.chat_data['messages']:
            if type(msg['text']) is str:
                tokens = word_tokenize(msg['text'])
                tokens = list(filter(lambda item : item not in self.stopword, tokens))
                
                text_content += f" {' '.join(tokens)}"

        text_content = self.normalizer.normalize(text_content)

        wordcloud = WordCloud(font_path=(str(DATA_DIR / 'NotoNaskhArabic-Regular.ttf'))).generate(text_content) 
        wordcloud.to_file(output_dir / 'result.png')




if __name__ == "__main__":
    chat_stats = ChatStatistics(chat_json=DATA_DIR / 'result.json')
    chat_stats.geanarate_word_cloud(output_dir=DATA_DIR) 
