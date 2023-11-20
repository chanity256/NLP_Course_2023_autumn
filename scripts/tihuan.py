# 读取原始文件
with open('/Users/tootough/PycharmProjects/NLP_Course_2023_autumn/output_sov_1.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

# 替换操作并在每一行结尾添加 "//"
modified_content = []
for line in content:
    modified_line = line.replace('^$', ' & ').rstrip() + " \\\\" + "\n"
    modified_content.append(modified_line)

# 将结果写入新文件
with open('tex_1.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(modified_content)
