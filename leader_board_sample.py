import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
from matplotlib.pyplot import imshow
from PIL import Image

img_train_path = "train/"
print(os.listdir("train"))
df = pd.read_csv("train.csv")
df['Image_path'] = \
    [os.path.join(img_train_path,whale) for whale in df['Image']]
df
# df.Id.unique()
label_map = df.Id.value_counts(ascending=True)
len(label_map)




