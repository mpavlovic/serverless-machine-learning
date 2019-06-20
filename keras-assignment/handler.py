print('container start')
try:
  import unzip_requirements
except ImportError:
  pass
print('unzip end')

import json
from keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import keras_applications
import boto3
import os
import tempfile
print('import end')

keras_applications.imagenet_utils.CLASS_INDEX = json.load(open('imagenet_class_index.json'))

MODEL_BUCKET_NAME = os.environ['MODEL_BUCKET_NAME']
MODEL_FILE_NAME_KEY = os.environ['MODEL_FILE_NAME_KEY']
TEMP_DIR = '/tmp' 
MODEL_PATH = os.path.join(TEMP_DIR, MODEL_FILE_NAME_KEY)
UPLOAD_BUCKET_NAME = os.environ['UPLOAD_BUCKET_NAME']

print('downloading model...')
s3 = boto3.resource('s3')
s3.Bucket(MODEL_BUCKET_NAME).download_file(MODEL_FILE_NAME_KEY, MODEL_PATH)

print('loading model...')
model = InceptionV3(weights=MODEL_PATH)
print('model loaded\n')


def classify(event, context):
    body = {}

    params = event['queryStringParameters']
    if params is not None and 'imageKey' in params:
        image_key = params['imageKey']

        # download image
        print('Downloading image...')
        tmp_image_file = tempfile.NamedTemporaryFile(dir=TEMP_DIR)
        img_object = s3.Bucket(UPLOAD_BUCKET_NAME).Object(image_key)
        img_object.download_fileobj(tmp_image_file)
        print('Image downloaded to', tmp_image_file.name)

        #  load and preprocess the image
        img = image.load_img(tmp_image_file.name, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0) 
        x = preprocess_input(x)
        tmp_image_file.close()

        # predict image classes and decode predictions
        predictions = model.predict(x)
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        predictions_list = []
        for pred in decoded_predictions:
            predictions_list.append({'label': pred[1].replace('_', ' ').capitalize(), 'probability': float(pred[2])})

        body['message'] = 'OK'
        body['predictions'] = predictions_list

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        }
    }

    return response
