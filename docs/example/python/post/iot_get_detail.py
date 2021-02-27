# -*- coding: utf-8 -*-

"""
  IoThook REST Api Test with Python

   When the code is run, verification is performed with APIKEY.
   Data about the device api_key is posted to IoThook.

   This example is at the initial level to send / receive data to the IotHook service.
   It aims to conduct tests.

   20 September 2017
   Update: 19 August 2019
   Sahin MERSIN

   For more

  http://www.iothook.com
  ve
  https://github.com/electrocoder/iotHook

  sitelerine gidiniz.

  Sorular ve destek talepleri icin
  https://github.com/electrocoder/iotHook/issues
  sayfasindan veya Meşe Bilişim den yardım alabilirsiniz.

  Yayin : http://mesebilisim.com

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

url = 'http://localhost:8000/api/datas/2324/'

for i in range(100):
    response = requests.get(url, headers=headers)
    pprint.pprint(response.json())
    time.sleep(5)
