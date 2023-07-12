import os

import openai
import soundfile as sf
import requests
import uuid

from config import config

def transcript_audio(media_url: str) -> dict:
    try:
        ogg_file_path = f'{config.OUTPUT_DIR}/{uuid.uuid1()}.ogg'
        data = requests.get(media_url)
        with open(ogg_file_path, 'wb') as file:
            file.write(data.content)
        audio_data, sample_rate = sf.read(ogg_file_path)
        mp3_file_path = f'{config.OUTPUT_DIR}/{uuid.uuid1()}.mp3'
        sf.write(mp3_file_path, audio_data, sample_rate)
        audio_file = open(mp3_file_path, 'rb')
        os.unlink(ogg_file_path)
        os.unlink(mp3_file_path)
        transcript = openai.Audio.transcribe(
            'whisper-1', audio_file, api_key=config.OPENAI_API_KEY)
        return {
            'status': 1,
            'transcript': transcript['text']
        }
    except Exception as e:
        print('Error at transcript_audio...')
        print(e)
        return {
            'status': 0,
            'transcript': transcript['text']
        }

def create_string_chunks(string, length):
    words = string.split()
    sentences = []
    temp_string= ''
    for w in words:
        if len(temp_string) > length:
            sentences.append(f'{temp_string}...')
            temp_string = ''
        temp_string += f'{w} '
    sentences.append(temp_string)
    return sentences
