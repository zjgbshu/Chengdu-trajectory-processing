import os
import pandas as pd
from datetime import datetime

# 输入文件夹路径和输出文件夹路径
input_dir = 'F:\MarineTraffic/nettraj/tptk\data/'
output_dir = 'F:\MarineTraffic/nettraj/tptk\data_source/'

# 获取文件夹内的所有txt文件
txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]


for txt_file in txt_files:
    j = 0
    # 读取txt文件到DataFrame中
    f = pd.read_csv(input_dir + txt_file, names=["id", "x", "y", "is", "time"], encoding='utf-8')

    state = 0
    for index, row in f.iterrows():

        # 将时间格式转换为标准格式
        # str = row['time']
        # datetime.strptime(str,'%Y/%m/%d %H:%M:%S')

        str = row['time']
        x = str.split(' ')
        t = x[0].split('/')
        t[1] = t[1].zfill(2)
        t[2] = t[2].zfill(2)
        str = t[0] + '-' + t[1] + '-' + t[2] + ' ' + x[1]
        f.loc[index, 'time'] = str

        # 按一定条件重新编号
        if row['is'] == 1:
            if state == 0:  # 如果上一行为0，增加j
                j += 1
                state = 1
            f.loc[index, 'id'] = j
        else:
            state = 0

    f = f.drop(f[f['is'] == 0].index)
    # 删除is列
    f = f.drop(columns=['is'])

    #将'x'与'time'进行交换
    f = f[['id', 'time', 'y', 'x']] # 将 'x' 和 'time' 列交换位置，同时保留原有列顺序

    # 将结果写入新的txt文件中
    new_file_name = txt_file.split('.')[0] + '.txt'
    f.to_csv(output_dir + new_file_name, index=False, header=False, encoding='utf-8')
    print('处理成功 '+new_file_name)
