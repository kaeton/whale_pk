import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
from matplotlib.pyplot import imshow
from PIL import Image
import shutil

print(os.listdir("../"))
img_train_path = "../input/train/"
img_newwhale_path = "../input/newwhale/"
print(os.listdir("../input/train")[:5])
df = pd.read_csv("../train.csv")

df['Image_path'] = \
    [os.path.join(img_train_path,whale) for whale in df['Image']]
new_whale = df[df["Id"] == "new_whale"]

[shutil.copy(os.path.join(img_train_path, imagename),
             os.path.join(img_newwhale_path, imagename))
 for imagename in new_whale["Image"]]
