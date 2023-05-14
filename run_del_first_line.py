import os

#TPTK清洗后，首行的注释信息需要删除

# 输入文件夹路径
folder_path = ""

# 输入保存目录路径
save_path = ""

# 获取文件夹内所有txt文件
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.txt')]

# 遍历每个txt文件
for file in files:
    # 读取文件内容
    with open(os.path.join(folder_path, file), 'r') as f:
        lines = f.readlines()
    # 删除第一行
    lines.pop(0)
    # 写入新文件
    with open(os.path.join(save_path, file), 'w') as f:
        f.writelines(lines)

print("删除完毕")
