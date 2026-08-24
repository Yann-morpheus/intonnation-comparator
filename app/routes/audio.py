from flask import request
from app.utils import success_response,error_response
from app.routes import audio_bp
from app.services.audio_analyser import compare_audio
from app.guard.files_guard import validate_audio_file
import os

# @audio_bp.route("/")
# def index():
#     return {"message": "api test"}

@audio_bp.route('/compare',methods=['POST'])
def postAudio():
    ref_file=request.files.get('reference')
    cand_file= request.files.get('candidate')
    validate_audio_file(ref_file)
    validate_audio_file(cand_file)
    try:
        ref_file_name = ref_file.filename    
        ref_file.save(ref_file_name)
        cand_file_name = cand_file.filename    
        cand_file.save(cand_file_name)
        result= compare_audio(ref_file_name,cand_file_name)
    except Exception as e:
        return error_response({"error":str(e)})    
    return success_response(data=result)

@audio_bp.route('/',methods=['GET'])
def getAudio():
    return 'ok'