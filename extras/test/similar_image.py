#importing libraries
import os
import numpy as np
import tensorflow as tf
from sklearn.neighbors import NearestNeighbors
from IO_utils import read_imgs_dir
from transform_utils import apply_transformer,resize_img, normalize_img
from plot_utils import plot_query_retrieval
from keras.applications.resnet50 import ResNet50


# Class for Appling transformations to all images
class ImageTransformer(object):

    def __init__(self, shape_resize):
        self.shape_resize = shape_resize

    def __call__(self, img):
        img_transformed = resize_img(img, self.shape_resize)
        img_transformed = normalize_img(img_transformed)
        return img_transformed

modelName='resnet50'


#taking input on number of similar images to be retreived

n=int(input("Number of similar images to be retreived: "))
# Make paths
DataTrain = os.path.join(os.getcwd(), "data", "train")
DataTest = os.path.join(os.getcwd(), "data", "test")
outDir = os.path.join(os.getcwd(), "output", modelName)


#creating path for output images

if not os.path.exists(outDir):
    os.makedirs(outDir)


# Read images
extensions = [".jpg", ".jpeg"]
print("Reading train images from '{}'...".format(DataTrain))
imgs_train = read_imgs_dir(DataTrain, extensions)
print("Reading test images from '{}'...".format(DataTest))
imgs_test = read_imgs_dir(DataTest, extensions)
shape_img = imgs_train[0].shape
print("Image shape = {}".format(shape_img))

#downloading resnet50 with imagenet weights
print("Loading resnet pre-trained model...")
model = ResNet50(weights='imagenet',include_top=False,input_shape=shape_img)
print(model.summary())


shape_img_resize = tuple([int(x) for x in model.input.shape[1:]])
input_shape_model = tuple([int(x) for x in model.input.shape[1:]])
output_shape_model = tuple([int(x) for x in model.output.shape[1:]])

# Print some model info
print("input_shape_model = {}".format(input_shape_model))
print("output_shape_model = {}".format(output_shape_model))
print("shape_img_resize = {}".format(shape_img_resize))





transformer = ImageTransformer(shape_img_resize)
print("Applying image transformer to training images...")
imgs_train_transformed = apply_transformer(imgs_train, transformer)
print("Applying image transformer to test images...")
imgs_test_transformed = apply_transformer(imgs_test, transformer)



# Convert images to numpy array
X_train = np.array(imgs_train_transformed).reshape((-1,) + input_shape_model)
X_test = np.array(imgs_test_transformed).reshape((-1,) + input_shape_model)
print(" -> X_train.shape = {}".format(X_train.shape))
print(" -> X_test.shape = {}".format(X_test.shape))





# Create embeddings using model
print("Inferencing embeddings using pre-trained model...")
E_train = model.predict(X_train)
E_train_flatten = E_train.reshape((-1, np.prod(output_shape_model)))
E_test = model.predict(X_test)
E_test_flatten = E_test.reshape((-1, np.prod(output_shape_model)))
print(" -> E_train.shape = {}".format(E_train.shape))
print(" -> E_test.shape = {}".format(E_test.shape))
print(" -> E_train_flatten.shape = {}".format(E_train_flatten.shape))
print(" -> E_test_flatten.shape = {}".format(E_test_flatten.shape))



print("Fitting k-nearest-neighbour model on training images...")
knn = NearestNeighbors(n_neighbors=n, metric="cosine")
knn.fit(E_train_flatten)



for i, emb_flatten in enumerate(E_test_flatten):
    _, indices = knn.kneighbors([emb_flatten])# find k nearest train neighbours
    #print(indices)
    img_query = imgs_test[i] # query image
    imgs_retrieval = [imgs_train[idx] for idx in indices.flatten()] # retrieval images
    
    img_array = img_to_array(img)
    #print(type(img_array))
    #print(img_array.dtype)
    retrievalFile = os.path.join(outDir, "{}_retrieval_{}.png".format(i,j))
    save_img(retrievalFile, img_array)
      
    outFile = os.path.join(outDir, "{}_retrieval_{}.png".format(modelName, i))
    #plot_query_retrieval(img_query, imgs_retrieval, outFile=None)
    plot_query_retrieval(img_query, imgs_retrieval, outFile)
    print("Similar images result saved on output folder")

    


