from flask_restful import Resource 
import pandas as pd
from flask import request
import sqlalchemy
import time
import json

import os


class Samples(Resource):
    '''class one liner'''

    def post(self):
        '''function one liner'''

        self.provided_study_id=request.json['study_id']
