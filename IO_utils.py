
import os
import skimage.io

# Read image
def read_img(filePath):
    return skimage.io.imread(filePath, as_gray=False)

# Read images with common extensions from a directory
def read_imgs_dir(dirPath, extensions):
    args = [os.path.join(dirPath, filename)
            for filename in os.listdir(dirPath)
            if any(filename.lower().endswith(ext) for ext in extensions)]
    
    imgs = [read_img(arg) for arg in args]
    return imgs

# Save image to file
def save_img(filePath, img):
    skimage.io.imsave(filePath, img)