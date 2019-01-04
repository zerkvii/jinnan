import os
import re

import pandas as pd

if __name__ == '__main__':
    filename = os.path.join(os.getcwd(), 'data', 'new_train.csv')
    train_frame = pd.read_csv(filename, sep=',')
    regex_map = {
        'A9': '.+:.+:.+',
        'A11': '.+:.+:.+',
        'A14': '.+:.+:.+',
        'A16': '.+:.+:.+',
        'A20': '.+-.+',
        'A24': '.+:.+:.+',
        'A26': '.+:.+:.+',
        'A28': '.+-.+',
        'B4': '.+-.+',
        'B5': '.+:.+:.+',
        'B7': '.+:.+:.+',
        'B9': '.+-.+',
        'B10': '.+-.+',
    }
    for col in train_frame.colunms:
        count = 0
        if col in regex_map.keys():
            for ele in train_frame[col]:
                if len(re.findall(regex_map[col], str(ele))) > 0:
                    count += 1
                else:
                    print(count, ele)
