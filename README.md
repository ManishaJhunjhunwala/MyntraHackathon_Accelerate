# Myntra Snaplook

This project is the prototype submission for Myntra's WeForShe Hackathon Theme Accelerate. We have worked on to accelerate the
product discoverability and personalisation of Myntra's products.
We have implemented the feature of automatically detecting the clothes worn by the actors from a live video on platforms like Youtube or social media(Instagram) , then fetching top ‘k’ similar apparels from Myntra’s database on a side panel, allowing users to directly buy/wishlist/discard the product.
Then Reverse Image Search is applied on the extracted cloth images from the videos using Deep learning Similarity Model. We have used OpenCV for video processing, ResNet50 Deep Learning Model, KNN algorithm for getting the top 'k' similar images of the query image and Django for demonstration of the product as the main technologies for the implementation.

*Step 1:*
Extract frames from a live running video

*Step 2:*
Detect the lead_artists from the video frames

*Step 3:*
Extract the clothes worn by these lead-artists

<h3>Result of Object Detection and Cloth Extraction</h3>

![alt text](https://github.com/ManishaJhunjhunwala/MyntraHackathon_Accelerate/tree/main/lead_artist/back_image1.jpg)
![alt text](https://github.com/ManishaJhunjhunwala/MyntraHackathon_Accelerate/tree/main/lead_artist/back_image3.jpg)
![alt text](https://github.com/ManishaJhunjhunwala/MyntraHackathon_Accelerate/tree/main/lead_artist/back_image5.jpg)

*Step 4:*
Reverse Image google search these clothing images in Myntra dataset OR find matching fashion images through the similarity network

## *Working of Similarity Model*

This model will find the n similar images from the training dataset of the input image. It leverages the feature extraction of pre-trained of resnet50
and KNN algorithm to find similar images.

## Libraries:

Keras,sklearn,skimage

## Workflow:

1. At first, pretrained resnet50 is used to extract features of images. Only the feature extraction layer of resnet50 was downloaded and all training images are passed through it.

2. After passing it through resnet50 , we have flattened it and fitted it through knn where we have used cosine distance. Number of neighbours will depend on user input.

3. All the test images will go to resnet50 and then it will get nearest neighbours from the previously fitted knn and the similar image will be stored in output folder.

## Folder strucutre:

**myntrahackathon.py** : It containes the core code. It needs to be invoked to process the video and get all similar images. We can customise how many similar images is needed to be fetched.

**data**: In this folder training data will reside in train folder. Query image will reside in test folder(you can keep as many as you want).

**output/resnet50**: this folder contains the results from similarity model and it will be created automatically.

**output_similarity_model**: this folder contains the final output with query images through video processing and its similar images.

**UI_wireframes** : It contains the design wireframes that we had proposed for the solution hack. It is created using Figma.

**lead_artist** : This folder contains the intermediate images of the lead artists extracted from the frames of the video. These images will serve as as input to the similarity model created using resnet50 and knn.

*Other files contains various utility functions that will be used in core program file.*
**IO_utils.py** : It contains utility functions to read images with common extensions from a directory and save images in a  directory.

**plot_utils.py**: It contains utility functions to plot the input and output images in the required format to demonstrate the results.

**transform_utils.py** : It contains various utility functions to transform the images like resizing, normalising etc.


<h3>Dataset</h3>
<p><a href="http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html" target="_blank">Deep Fashion Dataset</a> dataset for cloth retrieval.</p>

<h3>Result of Similarity Network</h3>

![alt text](https://github.com/ManishaJhunjhunwala/MyntraHackathon_Accelerate/blob/main/output_similarity_model/resnet50_retrieval_0.png)
![alt text](https://github.com/ManishaJhunjhunwala/MyntraHackathon_Accelerate/blob/main/output_similarity_model/resnet50_retrieval_1.png)

![alt text](https://github.com/ManishaJhunjhunwala/MyntraHackathon_Accelerate/blob/main/output_similarity_model/resnet50_retrieval_2.png)
![alt text](https://github.com/ManishaJhunjhunwala/MyntraHackathon_Accelerate/blob/main/output_similarity_model/resnet50_retrieval_4.png)

![alt text](https://github.com/ManishaJhunjhunwala/MyntraHackathon_Accelerate/blob/main/output_similarity_model/resnet50_retrieval_5.png)

