'''
Author: Alchemist
Date: 2023-04-12
LastEditTime: 2024-08-20
FilePath: /PyramidCoder-demo/server/server.py
Description: 

Copyright (c) 2023, All Rights Reserved. 
'''
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import base64
import json
import os


app = Flask(__name__)
CORS(app)

data_path = "./resources/"
gqa_anno = "gqa_programs_tot_no_plan_v4.json"
nlvr2_anno = "nlvr2_programs_tot_no_plan_v1.json"


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/get_examples', methods=['GET'])
def get_examples():
    dataset_name = request.args.getlist('dataset_name[]')
    response = []
    with open(os.path.join(data_path, gqa_anno),"r") as f:
        anno = json.load(f)
    num = 5
    for x in anno.values():
        item = {}
        imgs = []
        # import pdb; pdb.set_trace()
        for y in x['image']:
            with open(os.path.join(data_path, 'images/gqa', y), 'rb') as f:
                img = f.read()
            base64_img = base64.b64encode(img).decode('utf-8')
            imgs.append(base64_img)
        item['image'] = imgs
        item['question'] = x['question']
        item['queries'] = x['queries'].split('\n')
        item['ja_question'] = x['ja_question']
        item['ja_queries'] = x['ja_queries']
        item['codes'] = x['codes']
        response.append(item)
        num -= 1
        if num == 0:
            break
    
    with open(os.path.join(data_path, nlvr2_anno),"r") as f:
        anno = json.load(f)
    num = 5
    for x in anno.values():
        item = {}
        imgs = []
        # import pdb; pdb.set_trace()
        for y in x['image']:
            with open(os.path.join(data_path, 'images/nlvr2', y), 'rb') as f:
                img = f.read()
            base64_img = base64.b64encode(img).decode('utf-8')
            imgs.append(base64_img)
        item['image'] = imgs
        item['question'] = x['question']
        item['queries'] = x['queries'].split('\n')
        item['ja_question'] = x['ja_question']
        item['ja_queries'] = x['ja_queries']
        item['codes'] = x['codes']
        item['dialogVisible']  = False
        response.append(item)
        num -= 1
        if num == 0:
            break

    return jsonify(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
