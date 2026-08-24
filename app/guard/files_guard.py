from mutagen import File
FILE_EXTENSION = ["wav", "mp3", "flac"]
FILE_MAX_SIZE = 1024 * 1024 * 10
FILE_MIN_DURATION = 2
FILE_MAX_DURATION = 3 * 60


def verify_duration(audio):
    duration = audio.info.length
    if duration < FILE_MIN_DURATION or duration > FILE_MAX_DURATION:
        return {
            "result": False,
            "message": "la durée d'un fichier audio doit être comprise entre 2s et 3min",
        }
    return {
        "result": True,
        "message": "le fichier est correct",
    }


def is_allowed_extension(filename):
    result = "." in filename and filename.rsplit(".", 1)[1].lower() in FILE_EXTENSION
    if result:
        return {"result": result, "message": "le fichier est autorisé"}
    return {
        "result": result,
        "message": "extension de fichier est invalide (wav,mp3,flac)",
    }


def is_authorized_file_size(upload_file):
    if len(upload_file) == 0:
        return {
            "result": False,
            "message": "fichier vide",
        }
    if len(upload_file) > FILE_MAX_SIZE:
        return {"result": False, "message": "fichier trop volumineux"}
    return {"result": True, "message": "taille autorisé"}


def is_file_exist(file_storage):
    if file_storage is None:
        return {"result": False, "message": "un ou deux fichier sont manquant"}
    return {
        "result":True,
        "message":"un ou deux fichier sont manquant"
    }


def validate_audio_file(file_storage):
    result = is_file_exist(file_storage)
    if not result["result"]:
        return result["message"]
    result = is_allowed_extension(file_storage.filename or "")
    if not result["result"]:
        return result["message"]
    upload_file = file_storage.read()
    file_storage.seek(0)
    result = is_authorized_file_size(upload_file)
    if not result["result"]:
        return result["message"]
    try:
        audio = File(file_storage)
        if audio is None:
            return "Le fichier n'est pas un fichier audio valide"
        result = verify_duration(audio)
        if not result["result"]:
            return result["message"]
    except Exception as e:
        return f"Impossible de lire le fichier audio : {str(e)}"
    file_storage.seek(0)
    return None
