# 将txt文件转化为csv文件，方便后续简历知识图谱
import csv

# 读取txt文件并解析数据
input_file = "/Users/tootough/PycharmProjects/NLP_Course_2023_autumn/output_sov_1.txt"  # 请将 "input.txt" 替换为包含数据的文本文件路径

data = []
with open(input_file, 'r') as file:
    for line in file:
        parts = line.strip().split('$^')
        data.append(parts)

# 写入CSV文件
output_file = "tex_1.csv"  # 输出的CSV文件路径

with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # 写入CSV文件的第一行标题
    csv_writer.writerow(["Subject", "Verb", "Object"])

    # 写入数据行
    for row in data:
        csv_writer.writerow(row)

print(f"数据已成功转换为 {output_file}")
