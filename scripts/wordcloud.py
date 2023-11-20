# 用于绘制文献摘要的词云图

import nltk
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords
from string import punctuation
from tqdm import tqdm
import wordcloud
import matplotlib.pyplot as plt
from collections import Counter


def load_text(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        return file.read().replace('\n', ' ').replace('<<<<', ' ')

def remove_stopwords(tokens, stop_words):
    return [token for token in tokens if token not in stop_words]

def generate_wordcloud(tokens, output_path="wordcloud.png"):
    wordcloud = WordCloud(background_color="white")
    wordcloud.generate(" ".join(tokens))
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(output_path)
    plt.show()

def calculate_and_output_frequency(tokens, output_file_path="output_wordcloud.txt"):
    tokens_frequency = Counter(tokens)
    total_tokens = len(tokens)

    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        output_file.write("\n\nWord Frequency:\n")

        # 使用 tqdm 更新进度条
        with tqdm(total=total_tokens, desc="Calculating Word Frequency", position=0, leave=True) as pbar:
            for token, frequency in tokens_frequency.items():
                output_file.write(f"{token}: {frequency}\n")
                pbar.update(1)  # 更新进度条

    print("Results written to", output_file_path)

# 语料库路径
corpus_path = "result_MM_Pubtator.txt"

# 加载文本
text = load_text(corpus_path)

# 分词
tokens = word_tokenize(text.lower())

# 停用词处理
stop_words = set(stopwords.words('english'))
tokens = remove_stopwords(tokens, stop_words)
tokens = remove_stopwords(tokens, punctuation)

# 生成词云
generate_wordcloud(tokens)

# 排序
tokens = sorted(tokens)

# 输出分词结果到文件
with open("pubtator_keyword_output.txt", 'w', encoding='utf-8') as output_file:
    output_file.write("Tokenized Text:\n")
    output_file.write('\n'.join(tokens))

# 计算词频并输出到文件
calculate_and_output_frequency(tokens)
