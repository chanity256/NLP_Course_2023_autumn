## NLP_Course_2023_autumn
本项目包含《生物文本挖掘与知识发现（本硕贯通）》2023秋季课程，课程论文使用到的全部代码、各类文件和latex原文档。
- 所有的代码都在scripts文件夹（包括自己书写的；老师上课发布的）
- 所有用到的文档，以及output的文档，都在files文件夹
- 所有output的图片都在figures文件夹
- 本次使用了enhanced-subject-verb-object-extraction-master文件夹中的subject_verb_object_extract.py脚本。（原项目地址：github.com/rock3125/ enhanced-subject-verb-object-extraction）

## 各个脚本的详细功能
相关脚本的功能，已在各自的代码注释中注明，现在此简略说明
1. KG.py 用来生成相关实体的知识图谱
2. Pubtator_abstract.sh 用于爬取PMID，并通过PubTator抓取问现在要
3. count_entity.py 用于计算已经提取出的gene实体和disease实体
4. junfen.py 把提取了关键词的文献摘要均分成4份，因为spacy只能一次处理1000000 characters。而我们的文献摘要大概370多万个characters
5. keywords_query_pubtator.py 读取PubTator结果文件，根据“gene”和“disease”关键词生成命中句及其标注。
6. pubtator_keyword_my.py 将文献摘要文本中相应的gene实体和disease实体抽取出
7. pubtator_keyword_ wc_my.py 用来绘制gene实体和disease实体的词云图
8. pubtator_wc.py 输出文献摘要的分词结果和词云
9. sov_extract.py 实现三元组提取。与enhanced-subject-verb-object-extraction-master文件夹中的subject_verb_object_extract.py脚本内容一致
10. sov_test.py 本次项目没有使用
11. tihuan.py 把三元组文件中的符号替换成“ & ”方便后续填写到latex文件构建表格
12. ttr.py 计算文献摘要的TTR
13. txt2csv.py 把相应的三元组txt文件转换成csv文件，方便后续构建知识图谱
14. wordcloud.py 本次项目并未使用

## 各个图片
1. “KG”开头的都是相应实体的知识图谱
2. wordcloud.png 是文献摘要的词云图
3. pubtator_keyword _disease.png 是疾病实体的词云图
4. pubtator_keyword_gene.png 是基因实体的词云图

## 各个文件
1. output_diseaseEntity.txt 疾病实体的txt文件
2. output_diseaseEntity_rank.txt 疾病实体按出现频率排序
3. output geneEntity.txt 基因实体的txt文件
4. output_geneEntity_rank.txt 基因实体按出现频率排序
5. output_ttr.txt 文献摘要的ttr
6. pubtator_keyword_output.txt 文献摘要的分词文件
7. result_MM_Pubtator.txt PubTator提取到的包含实体的文献摘要
9. sov_input_1.txt、sov_input_2.txt、sov_input_3.txt、sov_input_4.txt 我们将tmp_pubtator_blca_key_query.txt产生的结果分为4份，方便进行后续的三元组提取
10. output_ sov_1.txt、output_sov_2.txt、output_sov_ 3.txt、output_sov 4.txt 提取的三元组txt文件
11. sov_1.csv、sov_2.csv、sov_3.csv、sov_4.csv 提取的三元组的csv文件，SOV.CSV是这四份文件合在一起的总文件，具体内容一样
12. tmp_pubtator_blca_key_query.txt 通过keywords_query_pubtator.py读取PubTator结果文件，根据“gene”和“disease”关键词生成命中句及其标注。
13. tex_1.txt 需要添加到latex文件中的表格数据 
