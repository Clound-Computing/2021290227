import os
import tqdm
from PIL import Image
import re
import json
import uuid
import random

def process_json_to_txt():

    if not os.path.exists('E:/vf/ython/cloud/final/processd_data'):
        os.makedirs('E:/vf/ython/cloud/final/processd_data')
    f_new = open('E:/vf/ython/cloud/final/processd_data/data.txt', 'a+')
    
    num = 0
    for i in tqdm.tqdm(range(6)):
        with open('E:/vf/ython/cloud/final/top_img/gossipcop_v3-{}.json'.format(i + 1), 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 为每个对象创建一个唯一的 'ID' 属性
        for item in data:
            item['ID'] = str(uuid.uuid4() + num)
        num = num + sum(1 for item in data.values() if item.get('has_top_img') == 1)

        # 提取所有的目标属性
        text = [item['generated_text'] for item in data.values() if item.get('has_top_img') == 1]
        label = [item['generated_labels'] for item in data.values() if item.get('has_top_img') == 1]
        ID = [item['ID'] for item in data.values()]
        has_attribute = any('origin_id' in item for item in data.values())
        if has_attribute:
            img_id = [item['origin_id'] + "_top_img.png" for item in data.values() if item.get('has_top_img') == 1]
        else:
            img_id1 = [item['doc_id1'] + "_top_img.png" for item in data.values() if item.get('has_top_img') == 1]
            img_id2 = [item['doc_id2'] + "_top_img.png" for item in data.values() if item.get('has_top_img') == 1]
            img_id = img_id1 + img_id2

        # 将提取的目标属性写入 TXT 文件
        f_new.write(ID + '|' + text + '|' + img_id + '|' + label + '\n')

    f_new.close()


def get_matrix():

    data = open('E:/vf/ython/cloud/final/processd_data/data.txt', 'a+')
    train_file = open('E:/vf/ython/cloud/final/processd_data/train.txt', 'a+')
    test_file = open('E:/vf/ython/cloud/final/processd_data/test.txt', 'a+')

    # 打乱数据顺序
    random.shuffle(data)

    # 计算分割点
    split_index = int(len(data) * 0.7)

    # 划分训练集和测试集
    train_data = data[:split_index]
    test_data = data[split_index:]


    # 将训练集写入 train.txt
    train_file.write(train_data)
    # 将测试集写入 test.txt
    test_file.write(test_data)

    print('数据集划分完成')

    data.close()
    train_file.close()
    test_file.close()

    return

if __name__ == '__main__':
    print('===>  process dataset......')
    if os.path.exists('E:/vf/ython/cloud/final/processd_data/train.txt'):
        os.remove('E:/vf/ython/cloud/final/processd_data/train.txt')
    if os.path.exists('E:/vf/ython/cloud/final/processd_data/test.txt'):
        os.remove('E:/vf/ython/cloud/final/processd_data/test.txt')
    if os.path.exists('E:/vf/ython/cloud/final/processd_data/data.txt'):
        os.remove('E:/vf/ython/cloud/final/processd_data/data.txt')
    process_json_to_txt()
    get_matrix()
