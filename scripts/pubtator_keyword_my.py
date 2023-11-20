# 用来在文献摘要文本中抽取出，相应的gene实体和disease实体

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re



# 读取 PubTator 文献摘要，将摘要文本存储在变量 abstract 中
with open('/Users/tootough/result_MM_Pubtator.txt', 'r', encoding='utf-8') as file:
    abstract = file.read()

# 使用句子划分函数将摘要分成句子
sentences = sent_tokenize(abstract)

# 初始化一个列表，用于存储抽取的基因名称
gene_names = []

# 迭代每个句子并进行基因名称抽取
for sentence in sentences:
    # 使用词语划分函数将句子分成单词
    words = word_tokenize(sentence)

    # 去除停用词

    words = [word for word in words if word.lower() not in stopwords.words('english')]


gene_entities = re.findall(r'(\S+)\s+Gene', abstract)

gene_entities = sorted(gene_entities)

# 将匹配到的基因名称写入文件
with open('output_GeneEntity.txt', 'w', encoding='utf-8') as output_file:
    for gene in gene_entities:
        output_file.write(gene + '\n')

print("Gene entities have been written to output_geneEntity.txt.")