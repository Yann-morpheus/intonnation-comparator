from flask import jsonify
from functools import wraps
import re

#  format de réponse api succès
def success_response(data=None,message="Success",status=200):
    response={
        'status':'success',
        'message':message
    }
    if data is not None:
        response['data']=data
    return jsonify(response),status  

#  format réponse api échec
def error_response(message="La requête a échoué",status=400, errors=None):
    response={
        'status':'echec',
        'message':message
    }
    if errors:
        response['errors']=errors
    return jsonify(response),status    