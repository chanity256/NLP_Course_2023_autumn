# 用于计算已经提取出的gene实体和disease实体

from collections import Counter

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = Counter(words)
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_count

def save_results_to_file(output_file, sorted_word_count):
    with open(output_file, 'w') as file:
        for word, count in sorted_word_count:
            file.write(f"{word}: {count}\n")

if __name__ == "__main__":
    input_file = "/PubtatorProject/output_diseaseEntity.txt"  # 请将 "your_file.txt" 替换为你要处理的文本文件的路径
    output_file = ("output_diseaseEntity_KG.txt")

    word_count = count_words_in_file(input_file)
    save_results_to_file(output_file, word_count)

    print(f"结果已保存到 {output_file}")
