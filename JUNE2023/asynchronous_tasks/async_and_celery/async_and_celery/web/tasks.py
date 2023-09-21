import time

import whisper
from celery import shared_task

from async_and_celery.web.models import Transcription


@shared_task
def transcribe_to_model(pk):
	model = whisper.load_model('base')
	transcription = Transcription.objects.filter(pk=pk).get()
	result = model.transcribe(
		transcription.audio.path,
		verbose=True,
		language='en',
		fp16=False,
	)
	transcription.text = result['text']
	transcription.save()


@shared_task
def example_background_job():
	print('example_job started')
	time.sleep(1.5)
	print('')
