
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# FOR TRAINING
# Create a train generator object that rescales 1/255 -> pixel value range of images between 0 (black) - 1 (white)
train_datagen = ImageDataGenerator(rescale= 1./255)

# Flow training images in 128 batch using train_datagen generator
train_generator = train_datagen.flow_from_directory(
        './horse-or-human/',
        target_size = (300,300),
        batch_size = 32,
        class_mode = "binary"
)

# FOR VALIDATION
# Create a validation generator object that rescale 1/255
validation_datagen = ImageDataGenerator(rescale = 1./255)

# Flow validation images in 32 batch using validation_datagen generator
validation_generator = validation_datagen.flow_from_directory(
        './validation-horse-or-human/',
        target_size = (300,300),
        batch_size = 32,
        class_mode = "binary"
)
