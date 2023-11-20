# 用于计算文献摘要的ttr
import nltk

# 读取文本文件
with open('/Users/tootough/result_MM_Pubtator.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 将文本分词
tokens = nltk.word_tokenize(text)

# 计算类型（不同单词的数量）
types = len(set(tokens))

# 计算标记（总单词数量）
tokens = [word for word in tokens if word.isalpha()]  # 去除标点符号等非字母字符
tokens = [word.lower() for word in tokens]  # 转换为小写以忽略大小写
tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  # 去除停用词

tokens_count = len(tokens)

# 计算TTR
ttr = types / tokens_count

# 保留TTR结果为两位小数
ttr = round(ttr, 2)

sorted_tokens = sorted(tokens)

# 输出结果到文件
with open('output_ttr.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"Types: {types}\n")
    output_file.write(f"Tokens: {tokens_count}\n")
    output_file.write(f"TTR: {ttr}\n")
    output_file.write("Words:\n")
    output_file.write("\n".join(sorted_tokens))  # 将单词列表写入文件

print(f"Types: {types}")
print(f"Tokens: {tokens_count}")
print(f"TTR: {ttr:.2f}")
