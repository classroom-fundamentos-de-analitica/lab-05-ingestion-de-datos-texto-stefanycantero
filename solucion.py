import os
import pandas as pd

def read_files(dir_path, sentiment, data_list):
    files = os.listdir(dir_path)
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(dir_path, file), 'r', encoding='utf-8') as f:
                text = f.read()
                data_list.append({'phrase': text, 'sentiment': sentiment})

def test():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(script_dir, 'data', 'test')
    test_data = []

    for sentiment in os.listdir(test_dir):
        sentiment_dir = os.path.join(test_dir, sentiment)
        if os.path.isdir(sentiment_dir):
            read_files(sentiment_dir, sentiment, test_data)

    test_df = pd.DataFrame(test_data)

    return test_df

def train():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    train_dir = os.path.join(script_dir, 'data', 'train')
    train_data = []    

    for sentiment in os.listdir(train_dir):
        sentiment_dir = os.path.join(train_dir, sentiment)
        if os.path.isdir(sentiment_dir):
            read_files(sentiment_dir, sentiment, train_data)

    train_df = pd.DataFrame(train_data)

    return train_df

def save_csv(df, filename):
    df.to_csv(filename, index=False)

if __name__ == '__main__':
    test_df = test()
    train_df = train()
    save_csv(test_df, 'test_dataset.csv')
    save_csv(train_df, 'train_dataset.csv')