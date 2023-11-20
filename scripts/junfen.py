# 把提取了关键词的文献摘要均分成4份，因为spacy只能一次处理1000000 characters。而我们的文献摘要大概370多万个characters


# 打开输入文件
with open('tmp_pubtator_blca_key_query.txt', 'r') as input_file:
    content = input_file.read()

# 计算字符总数和均分成4个部分的字符数
total_chars = len(content)
chars_per_file = total_chars // 4

# 分割文本并创建四个输出文件
for i in range(4):
    start = i * chars_per_file
    end = (i + 1) * chars_per_file

    # 处理最后一个文件，以确保不丢失任何字符
    if i == 3:
        end = total_chars

    # 获取分割后的文本段落
    document_content = content[start:end]

    # 创建输出文件
    output_filename = f'sov_input_{i + 1}.txt'
    with open(output_filename, 'w') as output_file:
        output_file.write(document_content)

print("文档已成功分割成四个文件。")
