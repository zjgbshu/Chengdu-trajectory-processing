import os
import pandas as pd

#将3.删列未排号数据，按轨迹段进行分割

# 输入文件夹路径和输出文件夹路径
input_dir = 'D:/Nettraj/Chengdu201408/3.1删列排号未换列数据/20140819/'
output_dir = 'D:/Nettraj/Chengdu201408/4.按轨迹细分数据/20140819/'

# 获取文件夹内的所有txt文件
txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
file=os.listdir(input_dir)
num=len(file)
# str(num)
k=0

for txt_file in txt_files:
    # 读取txt文件到DataFrame中
    f = pd.read_csv(input_dir + txt_file, names=["id", "x", "y", "time"], encoding='utf-8')

    # 获取第一列中所有的关键字
    keywords = f.iloc[:, 0].unique()

    # 将数据按照关键字拆分成多个DataFrame，并保存到不同的txt文件中
    for keyword in keywords:
        temp_f = f[f.iloc[:, 0] == keyword]
        #根据关键字命名
        temp_f.to_csv(output_dir + txt_file.split('.')[0]+'_'+f'{keyword}.txt',sep="," , index=False ,header=None)

    #查看进度
    k+=1
    print('已分离'+str(k)+' / '+str(num))
    # print('处理成功 '+new_file_name)
