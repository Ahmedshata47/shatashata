from PIL import Image
import numpy as np
import pandas as pd


image = Image.open("f0d81115-fe52-4c73-8b64-f6ac12b09eab.jpg")
#image_rgb = image.convert("RGB")

arr = np.array(image)
#print(arr.shape)
height, width, channels = arr.shape
flattened_array = arr.reshape(-1, channels)
#print(flattened_array.shape)
df = pd.DataFrame(flattened_array,columns=["Red", "Green", "Blue"])
csv_file=df.to_csv("photo.csv")