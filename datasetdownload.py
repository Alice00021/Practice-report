import pandas as pd
import os
from openimages.download import download_dataset
# Загрузка файла с классами
class_descriptions = pd.read_csv('https://storage.googleapis.com/openimages/2018_04/class-descriptions-boxable.csv', header=None)

# Поиск идентификатора для белки
squirrel_id = class_descriptions[class_descriptions[1].str.contains('Squirrel')][0].values[0]
print(f"Squirrel class ID: {squirrel_id}")

# Создайте директорию для сохранения данных
output_dir = 'open_images_squirrel'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Загрузите изображения и аннотации
download_dataset(output_dir, class_labels=[squirrel_id], annotation_format='pascal', limit=100) 



download_dataset("/home/alice", ["Hammer", "Scissors",], annotation_format="pascal")