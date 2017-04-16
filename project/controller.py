
from flask import json, request

from tensor_flow_models.tutorials.image.imagenet import classify_image_on_server as ci

from project import app

@app.route('/caption_image', methods=['POST','GET'])
def caption_image():
    file = request.files['image_file']
    if file:
        response = ci.run_inference_on_image_data(file.read())
    else:
        response = {}
    print response
    return json.dumps(response)