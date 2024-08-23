"""
There are 2 code blocks for 2 different browser: Google and Safari. 
Run juct one of code blocks according to browser you use.
"""

# FOR GOOGLE 
import numpy as np
from google.colab import files
from tensorflow.keras.utils import load_img, img_to_array

uploaded = files.upload()

for fn in uploaded.keys():
 
  # predicting images
  path = '/content/' + fn
  img = load_img(path, target_size=(300, 300))
  x = img_to_array(img)
  x /= 255
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  if classes[0]>0.5:
    print(fn + " is a human")
  else:
    print(fn + " is a horse")



# FOR SAFARI
"""
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
import os

images = os.listdir("/tmp/images")

print(images)

for i in images:
  print()
# predicting images
  path = '/tmp/images/' + i
  img = load_img(path, target_size=(300, 300))
  x = img_to_array(img)
  x /= 255
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  if classes[0]>0.5:
    print(i + " is a human")
  else:
    print(i + " is a horse")
    """

    