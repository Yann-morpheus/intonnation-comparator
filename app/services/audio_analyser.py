import parselmouth as ps
import os
import numpy as np
from dtw import dtw


DEFAULT_TIME_STEP = 0.01
MAX_AUDIO_FREQUENCE = 500
MIN_AUDIO_FREQUENCE = 75
SCALE = 2.0
AUDIO_CAND_TEST = r"C:/Users/tttt/Desktop/notera/DADJU/La vérité.mp3"
AUDIO_REF_TEST = r"C:/Users/tttt/Desktop/notera/DADJU/La vérité.mp3"
# AUDIO_REF_TEST = r"C:/Users/tttt\Desktop/intonation_compatibility/test1.mp3"
# AUDIO_CAND_TEST = r"C:/Users/tttt\Desktop/intonation_compatibility/test1.mp3"        
    
def extract_pitch(audio):
    sound = ps.Sound(audio)
    pitch = sound.to_pitch(
        time_step=DEFAULT_TIME_STEP,
        pitch_floor=MIN_AUDIO_FREQUENCE,
        pitch_ceiling=MAX_AUDIO_FREQUENCE,
    )
    values = pitch.selected_array["frequency"]
    # nettoyage des valeurs et de lacourbe
    values = values.copy()
    voiced = values > 0
    if voiced.sum() == 0:
        return "cet audio est silencieux ou trop bruité : aucun segment voisé détecté"
    indices = np.arange(len(values))
    values[~voiced] = np.interp(indices[~voiced], indices[voiced], values[voiced])
    return values


def extract_intensity(audio):
    sound = ps.Sound(audio)
    intensity = sound.to_intensity()
    return intensity.values[0]


def normalize_curve(values: np.ndarray):
    mean = np.mean(values)
    std = np.std(values)
    if std == 0:
        return np.zeros_like(values)
    return (values - mean) / std


def temporal_align(reference, candidate):
    alignment = dtw(candidate, reference, keep_internals=True, step_pattern="symmetric2")
    normalized_distance = alignment.normalizedDistance
    return {
        "distance": alignment.distance,
        "normalized_distance": normalized_distance,
        "path_reference": alignment.index2,
        "path_candidate": alignment.index1,
    }


def score_similitude(normalized_distance):
    score = 100 * np.exp(-normalized_distance / SCALE)
    return round(np.clip(score, 0.0, 100),2)


def global_score(scores):
    #  dans ce cas l'intensité et l'intonnation ont lemême poids pour la moyenne
    return   {
        'score global':str(sum(scores)/2)+'%',
        'details intonnation': str(scores[0])+'%',
        'details intensité': str(scores[1])+'%' 
        }
    
def compare_audio(audio_cand,audio_ref):
    # pitch 
    ref_pitch= normalize_curve( extract_pitch(audio_ref))
    cand_pitch=normalize_curve(extract_pitch(audio_cand))
    pitch_alignement=temporal_align(ref_pitch,cand_pitch);
    pitch_score= score_similitude(pitch_alignement['normalized_distance'])
    print('le taux de similitude au niveau de l\'intonnation est de :'+  str(pitch_score)+'%')
    #  intensité
    ref_intensity= normalize_curve( extract_intensity(audio_ref))
    cand_intensity=normalize_curve(extract_intensity(audio_cand))
    intensity_alignement=temporal_align(ref_intensity,cand_intensity);
    intensity_score= score_similitude(intensity_alignement['normalized_distance'])
    print('le taux de similitude au niveau de l\'intensité est de :'+  str(intensity_score)+'%')
    return {
        'pitch_score':pitch_score,
        'intensity_score':intensity_score
    }


compare_audio(AUDIO_CAND_TEST,AUDIO_REF_TEST)