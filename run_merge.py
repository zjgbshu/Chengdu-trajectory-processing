import os
import pandas as pd
from datetime import datetime

# 遍历若干个指定的文件夹，把所有同id的不同时间的txt合并起来，并且首列依次重排序
# 最多数量的文件夹为14865

# 输入文件夹路径和输出文件夹路径
input_dir = ''
output_dir = ''

i = 1
# i指向车辆id，j指向日期，k指向轨迹id，x指向新排序的轨迹id

# 循环最多14865个id
for i in range(1000, 7000):  # 左闭右开
    # 设置空表
    f = pd.DataFrame(data=None, index=None, columns=None)
    j = 18
    x = 1  # 新序号id
    for j in range(18, 31):  # 日期为18~30号
        # 循环最多2000条轨迹
        for k in range(1, 2000):
            if os.path.exists(
                    input_dir + '201408' + str(j) + '/201408' + str(j) + '_' + str(i) + '_' + str(k) + '.txt'):
                fx = pd.read_csv(
                    input_dir + '201408' + str(j) + '/201408' + str(j) + '_' + str(i) + '_' + str(k) + '.txt',
                    names=["time", "lat", "long"],
                    encoding='utf-8')
                # 增加新的一列，轨迹id
                fx.loc[:, 'id'] = x
                # axis=0代表纵向合并
                f = pd.concat([f, fx], axis=0)
                x = x + 1
    if f.empty:
        print(str(i) + '为空')
    else:
        # 改为时间戳
        f['timestamp'] = f['time'].apply(lambda x: int(datetime.timestamp(datetime.strptime(x, '%Y/%m/%d %H:%M:%S'))))
        # 更改列位置
        f = f[['id', 'long', 'lat', 'timestamp']]
        # 更改列名
        f.columns = ['id', 'x', 'y', 'timestamp']
        f.to_csv(output_dir + str(i) + '.csv', sep=";", index=False, header=True, mode='w', encoding='utf-8')
        print('已完成 ' + str(i) + '/14865')
