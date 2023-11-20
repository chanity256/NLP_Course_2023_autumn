# 用来绘制gene实体和disease实体的词云图

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 从 output_geneEntity.txt 文件中读取基因名称
with open('/Users/tootough/PycharmProjects/PubtatorProject/output_diseaseEntity.txt', 'r', encoding='utf-8') as input_file:
    gene_entities = input_file.read().splitlines()

# 将基因名称列表转换为字符串
gene_entities_text = ' '.join(gene_entities)

# 创建一个WordCloud对象
wordcloud = WordCloud(background_color='white').generate(gene_entities_text)

# 绘制词云图
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('/Users/tootough/PycharmProjects/PubtatorProject/pubtator_keyword_disease.png')
plt.show()
