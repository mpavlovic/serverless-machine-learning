# serverless-machine-learning
Examples of deploying machine learning models to AWS Lambda with Serverless framework and Python 3.

## Contents
### hello-world
Hello World example of creating a project with Serverless and deploying to AWS Lambda in Python.

### scikit-example
An example of Serverless project which contains machine learning regression model from scikit-learn trained on California housing dataset.

### spacy-example
An example of Serverless project which uses a small English model from spaCy NLP framework to create an AWS Lambda endpoint for named entity recognition. NOTE: .requirements.zip file created with serverless-python-requirements is omitted due to its size.

### spacy-assignment
An example of Serverless project which uses a small English model from spaCy NLP framework to create an AWS Lambda endpoint for parts of speech tagging and dependency parsing. NOTE: .requirements.zip file created with serverless-python-requirements is omitted due to its size.

### keras-example
An example of Serverless project which uses ResNet50 computer vision deep learning model from Keras framework to create an AWS Lambda endpoint for image recognition. The example requires two S3 buckets (one for model storage and other for image uploads) and optional AWS Identity Pool configuration. In `tensorflow` and `PIL` folders `.so` files are omitted due to their size. You should replace those folders with complete `tensorflow` and `PIL` installations. 

### keras-assignment
An example very similar to above keras-example, but uses InceptionV3 model instead of ResNet50.

### web-gui-code
Contains a web page for sending requests to endpoints created with above examples. You have to create your own endpoints and add their URLs and other credentials to `js/app.js` file.
