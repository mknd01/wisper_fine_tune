import pandas
import os 

def write_to_file(dataframe_path: str, path: str, filename: str):
    data_frame = pandas.read_csv(dataframe_path)
    if not os.path.exists(path):
        os.makedirs(path)
    file = os.path.join(path, filename)
    with open(file=file, mode='a') as f:
        for index, row in data_frame.iterrows():
            cols = list(data_frame.columns)
            for j in range(len(cols)):
                temp = row[cols[j]]
                temp = temp.split(' ')
                temp = ' '.join(temp)
                f.write(temp)
                if(j<len(cols)-1):
                    f.write('\t')
            f.write('\n')

write_to_file('test.csv', 'test', 'test')
write_to_file('train.csv', 'train', 'train')