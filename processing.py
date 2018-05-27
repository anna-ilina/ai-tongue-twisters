import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types



def speech_to_text(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    file_name = os.path.join(
        os.path.dirname(__file__),
        'audio_files',
        speech_file)

    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
























    # # Instantiates a client
    # client = speech.SpeechClient()
    #
    # # The name of the audio file to transcribe
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'audio_files',
    #     name)
    #
    # # Loads the audio into memory
    # with io.open(file_name, 'rb') as audio_file:
    #     content = audio_file.read()
    #     audio = types.RecognitionAudio(content=content)
    #
    # # In practice, stream should be a generator yielding chunks of audio data.
    # stream = [content]
    # requests = (types.StreamingRecognizeRequest(audio_content=chunk)
    #             for chunk in stream)
    #
    # config = types.RecognitionConfig(
    #     encoding='LINEAR16',
    #     sample_rate_hertz=16000,
    #     language_code='en-US'
    #     # speech_contexts=[speech.types.SpeechContext(
    #     #     phrases=["sheshells by the sheshore"],
    #     # )]
    #     )
    #  #   speech_contexts=phrase_hints)
    # streaming_config = types.StreamingRecognitionConfig(config=config)
    #
    # # partial_result = types.StreamingRecognitionResult()
    #
    # # streaming_recognize returns a generator.
    # responses = client.streaming_recognize(streaming_config, requests)
    #
    # for response in responses:
    #     # Once the transcription has settled, the first result will contain the
    #     # is_final result. The other results will be for subsequent portions of
    #     # the audio.
    #     for result in response.results:
    #         print('Finished: {}'.format(result.is_final))
    #         print('Stability: {}'.format(result.stability))
    #         alternatives = result.alternatives
    #         # The alternatives are ordered from most likely to least.
    #         for alternative in alternatives:
    #             print('Confidence: {}'.format(alternative.confidence))
    #             print(u'Transcript: {}'.format(alternative.transcript))
    #             return alternative.transcript

                # for word_info in alternative.words:
                #     word = word_info.word
                #     start_time = word_info.start_time
                #     end_time = word_info.end_time
                #     print('Word: {}, start_time: {}, end_time: {}'.format(
                #         word,
                #         start_time.seconds + start_time.nanos * 1e-9,
                #         end_time.seconds + end_time.nanos * 1e-9))



def find_error(target, transcription):
    if target == transcription:
        return True
    return False



print(find_error('she sells seashells by the seashore', speech_to_text('tt1_w.wav')))