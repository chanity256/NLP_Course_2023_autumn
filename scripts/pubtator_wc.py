# 用于生成抓取了包含gene和disease实体的句子和短语的词云图。但是最终没有使用。
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords
from string import punctuation
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter


def load_text(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        return file.read().replace('\n', ' ').replace('<<<<', ' ')

def remove_stopwords(tokens, stop_words):
    # 去除标点符号和数字
    tokens = [token for token in tokens if token.isalpha()]
    return [token for token in tokens if token not in stop_words]
def generate_wordcloud(tokens, output_path="wordcloud.png"):
    wordcloud = WordCloud(background_color="white")
    wordcloud.generate(" ".join(tokens))
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(output_path)
    plt.show()

def calculate_and_output_frequency(tokens, output_file_path="pubtator_keyword_output.txt"):
    tokens_frequency = Counter(tokens)
    total_tokens = len(tokens)

    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        output_file.write("\n\nWord Frequency:\n")


    print("Results written to", output_file_path)

# 语料库路径
corpus_path = "/Users/tootough/Downloads/tmp_pubtator_blca_key_query.txt"

# 加载文本
text = load_text(corpus_path)

# 分词
tokens = word_tokenize(text.lower())

stop_words = set(stopwords.words('english'))

# 分词
tokens = word_tokenize(text.lower())

# 去除标点符号和数字
tokens = remove_stopwords(tokens, stop_words)


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
