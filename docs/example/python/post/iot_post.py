# -*- coding: utf-8 -*-

"""
  Python ile IoThook REST Api Testi

   When the code is run, verification is performed with APIKEY.
   Data about the device api_key is posted to IoThook.

   This example is at the initial level to send / receive data to the IotHook service.
   It aims to conduct tests.

  20 September 2017
   Update: 19 August 2019
  Sahin MERSIN

  For more

  http://www.iothook.com
  and
  https://github.com/electrocoder/iotHook

  go to their website.

  For questions and support requests
  https://github.com/electrocoder/iotHook/issues
  page or you can get help from Meşe Bilişim.

  Website : http://mesebilisim.com

  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

  http://www.apache.org/licenses/
"""

import json
import pprint
import random
import time

import requests

headers = {'Content-type': 'application/json'}

url = 'http://localhost:8000/api/datas/'

for i in range(10):
    data = {
        'api_key': '48e7b9391768dfa979299372',
        'field_1': random.randint(1, 10),
        'field_2': round(random.uniform(0.0,10.0), 2),
    }

    data_json = json.dumps(data)

    response = requests.post(url, data=data_json, headers=headers)
    pprint.pprint(response.json())
    time.sleep(5)
