import requests

# URLs
urls = [
    "https://storage.googleapis.com/tensorflow-1-public/course2/week3/horse-or-human.zip",
    "https://storage.googleapis.com/tensorflow-1-public/course2/week3/validation-horse-or-human.zip"
]

# Download process
for url in urls:
    response = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"{filename} downloaded.")


import zipfile

# Unzip training set
local_zip = './horse-or-human.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('./horse-or-human')
zip_ref.close()

# Unzip validation set
local_zip = './validation-horse-or-human.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('./validation-horse-or-human')
zip_ref.close()

import os

# Training horse pitcures directory
train_horse_dir = os.path.join('./horse-or-human/horses')

# Training human pictures directory
train_human_dir = os.path.join('./horse-or-human/humans')

# Validation horse pitcures directory
validation_horse_dir = os.path.join('./validation-horse-or-human/horses')

# Validation human pictures directory
validation_human_dir = os.path.join('./validation-horse-or-human/humans')



# Number of images for each train directory
print('Total training horse pitcures:', len(os.listdir(train_horse_dir)))
print('Total training human pitcures:', len(os.listdir(train_human_dir)))

print('Total validation horse pitcures:', len(os.listdir(validation_horse_dir)))
print('Total validation human pitcures:', len(os.listdir(validation_human_dir)))



# Check files names training set images and see 10 examples

train_horse_names = os.listdir(train_horse_dir)
print(train_horse_names[:10])

train_human_names = os.listdir(train_human_dir)
print(train_human_names[:10])

# Check files names of validation set images and see 10 examples
validation_horse_names = os.listdir(validation_horse_dir)
print(validation_horse_names[:10])

validation_human_names = os.listdir(validation_human_dir)
print(validation_human_names[:10])



# Display 8 horse and 8 human images
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Parameters for graph; we'll output images in a 4x4 configuration
nrows = 4
ncols = 4

# Index for iterating over images
pic_index = 0

# Set up matplotlib fig, and size it to fit 4x4 pics
fig = plt.gcf()
fig.set_size_inches(ncols * 4, nrows * 4)

pic_index += 8
next_horse_pix = [os.path.join(train_horse_dir, fname) 
                for fname in train_horse_names[pic_index-8:pic_index]]
next_human_pix = [os.path.join(train_human_dir, fname) 
                for fname in train_human_names[pic_index-8:pic_index]]

for i, img_path in enumerate(next_horse_pix+next_human_pix):
  # Set up subplot; subplot indices start at 1
  sp = plt.subplot(nrows, ncols, i + 1)
  # Don't show axes (or gridlines)
  sp.axis('Off') 

  img = mpimg.imread(img_path)
  plt.imshow(img)

plt.show()