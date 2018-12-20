import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
from matplotlib.pyplot import imshow
from PIL import Image

print(os.listdir("../"))
img_train_path = "../input/train/"
print(os.listdir("../input/train")[:5])
df = pd.read_csv("../train.csv")

df['Image_path'] = \
    [os.path.join(img_train_path,whale) for whale in df['Image']]
new_whale = df[df["Id"] == "new_whale"]

plt.interactive(False)

for new_whale_label in new_whale["Image_path"].head(n=2):
    print(new_whale_label)
    img = Image.open(new_whale_label)
    plt.imshow(img)
    plt.show(block=True)
    # plt.show()
