# 用来生成相关实体的知识图谱

import networkx as nx
import csv
import matplotlib.pyplot as plt


# 创建一个有向图
G = nx.DiGraph()



# 从CSV文件中读取数据并添加到图中
csv_file = "/Users/tootough/PycharmProjects/PubtatorProject/sov.csv"  # 请将 "data.csv" 替换为包含数据的CSV文件的路径

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # 跳过标题行

    for row in csv_reader:
        if len(row) >= 3:  # 确保行包含至少三个值
            subject, verb, obj = row
            if 'cancer' in subject or 'cancer' in obj:
                G.add_edge(subject, obj, action=verb)

# 使用 NetworkX 绘制图谱
pos = nx.spring_layout(G)  # 定义节点布局

plt.figure(figsize=(12, 12))
# 定义节点颜色，subject 为蓝色，object 为绿色
node_colors = ['blue' if 'cancer' in node else 'green' for node in G.nodes]

nx.draw(G, pos, with_labels=True, node_size=300, node_color=node_colors, font_size=10, font_weight='bold', arrowsize=20)
labels = nx.get_edge_attributes(G, 'action')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, font_color='red')
plt.title("知识图谱")
plt.axis('off')

# 保存图谱到 "sov.png"
plt.savefig("KG_cancer.png")

# 显示图谱（可选）
plt.show()

# 打印所有节点
print("Nodes:")
for node in G.nodes():
    print(node)

# 打印所有边
print("\nEdges:")
for edge in G.edges():
    print(edge)
