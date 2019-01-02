import os
import re

import pandas as pd


def get_num(str):
    """
    :param str: str
    :return: int
    """
    return int(re.findall('[0-9]+', str)[0])


def sort_by_id(dataframe):
    """
    :param dataframe:pd.dataframe
    :return: pd.data.frame
    """
    dataframe['样本id'] = dataframe['样本id'].apply(get_num)
    return dataframe.sort_values('样本id')


if __name__ == '__main__':
    filename = os.path.join(os.getcwd(), 'tc', 'data', 'test.csv')
    savefile = os.path.join(os.getcwd(), 'tc', 'data', 'new_test.csv')
    test = pd.read_csv(filename, sep=',',encoding='gbk')
    data = sort_by_id(dataframe=test)
    data.to_csv(savefile, index=0)
