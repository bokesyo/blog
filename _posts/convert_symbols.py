import re

def replace_dollars_in_file(file_path):
    # 读取原始文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式替换$xxx$为\[xxx\]，但跳过$$xxx$$
    modified_content = re.sub(r'(?<!\$)\$(.+?)\$(?!\$)', r'\\[\1\\]', content)

    # 将修改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# 使用示例
file_path = '/home/ubuntu/bokesyo.github.io/_posts/2023-12-25-rlllm.md'  # 替换为你的文件路径
replace_dollars_in_file(file_path)
