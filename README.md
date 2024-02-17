# MNIST-CNN-and-Transformers-Webpage
This repository showcases a collaborative project undertaken as part of the Optimisation Course in the Master's program for Business Analytics at the McCombs School of Business, University of Texas at Austin.
**Collaborators:** Meenakshi Sundaram, Saiyam Shah, Eeshana Hamed


**1. Overview**
This project aims to develop and compare the performance of two different neural network architectures, Convolutional Neural Network (CNN) and Transformer Neural Network, on the MNIST dataset and showcase the results obtained in webpage using Anvil. 

**2. Neural Network Architectures**
Built a model using CNN and Trnasformers.
*Convolutional Neural Network (CNN):*
Explored multiple convolutional layers with varying filter sizes and numbers of filters.
Used max-pooling layers for downsampling.
Employed dense layers with dropout regularization.
**Achieved 99+ accuracy**

*Transformer Neural Network:*
Implemented a Transformer architecture with Multi-Head Self-Attention (MHSA) layers.
Experimented with different hidden, key/query, and value dimensions.
Tuned the number of attention heads and layers.
**Achieved 98.6% accuracy**

**3. Web Application Features**
*User Authentication:*

Users are required to sign in with their email and password.
An account is created for them if necessary.

*Model Descriptions:*

Detailed descriptions of the CNN and Transformer architectures are provided.
Explanation of the differences between the two models.

*Upload and Classification:*

Users can upload a CSV file containing pixel intensities of a 28x28 image.
The uploaded image is classified using both CNN and Transformer models.
Classification results are displayed on the webpage.

*Analysis and Comparison:*

Misclassified images are plotted along with their correct and predicted labels.
Analysis of common misclassifications and potential reasons behind them.

**4. Hosting and Deployment**

*Anvil Web Application:*

The web application is developed using Anvil.
The app is published at https://MSBAoptim2-22.anvil.app

*Backend Code Hosting:*

The backend code, including TensorFlow models, is hosted on AWS Lightsail.
Instructions for accessing the cloud server and running the backend code are provided in this repo.
