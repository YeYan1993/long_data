import pandas as pd
import numpy as np
import re

if __name__ == '__main__':
    inter_data = pd.read_table("data2/intersectGenes.txt")
    symbol_data = pd.read_table("data2/symbol.txt")
    time_data = pd.read_table("data2/time.txt")

    print(time_data.head())

    gene_name = np.array(inter_data['Gene'])
    # gene_name 在symbol文件中的id中找到对应的表达值
    gene_index = []
    for i in range(len(symbol_data['id'])):
        for ii in range(len(gene_name)):
            if symbol_data['id'][i] == gene_name[ii]:
                gene_index.append(i)

    # 重新构建一个Dataframe（关于symbol）
    new_symbol_data = symbol_data.iloc[gene_index,:]
    # new_symbol_data.to_csv('new_symbol_data.csv')
    # print(new_symbol_data)
    # new_symbol_data = pd.read_csv('new_symbol_data.csv')

    # 将dataframe行列转置
    transpose_data = new_symbol_data.T
    transpose_data.columns = new_symbol_data['id']

    transpose_data = transpose_data.iloc[2:,:]
    print(transpose_data)

    true_id = [id[0:12] for id in transpose_data.index]
    transpose_data['id'] = true_id


    # 合并
    new_time_data = time_data.merge(transpose_data,left_on='Id',right_on='id')
    # 去掉id那一列
    new_time_data = new_time_data.drop(['id'],axis=1)
    new_time_data.to_csv('new_time_2.csv')




