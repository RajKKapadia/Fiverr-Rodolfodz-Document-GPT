import time

from fastapi import APIRouter, Request

from document_gpt.helper.conversation import create_conversation
from document_gpt.helper.twilio_api import send_message
from document_gpt.helper.utils import transcript_audio, create_string_chunks

from config import config

router = APIRouter(
    prefix='',
    responses={404: {"description": "Not found"}}
)

@router.get('/')
async def home():
    return 'OK', 200

@router.post('/twilio')
async def twilio(request: Request):
    try:
        data = await request.form()
        print(data)
        print(data)
        query = data['Body']
        sender_id = data['From']
        print(f'Sender id - {sender_id}')
        # TODO
        # get the user
        # if not create
        # create chat_history from the previous conversations
        # quetion and answer
        if 'MediaUrl0' in data.keys():
            transcript = transcript_audio(data['MediaUrl0'])
            if transcript['status'] == 1:
                print(f'Query - {transcript["transcript"]}')
                response = create_conversation(transcript['transcript'], [])
            else:
                response = config.ERROR_MESSAGE
        else:
            print(f'Query - {query}')
            response = create_conversation(query, [])
        print(f'Response - {response}')
        if len(response) > 1600:
            sentences = create_string_chunks(response, 1500)
            for s in sentences:
                send_message(sender_id, s)
                time.sleep(2)
        else:
            send_message(sender_id, response)
        print('Message sent.')
    except Exception as e:
        print(e)

    return 'OK', 200
