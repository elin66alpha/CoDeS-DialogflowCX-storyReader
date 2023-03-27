import argparse
import uuid

from google.cloud.dialogflowcx_v3.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3.types import audio_config
from google.cloud.dialogflowcx_v3.types import session
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
from playsound import playsound

response_num = 0

# [START dialogflow_detect_intent_audio]
def run_sample():
    project_id = "yilin-test-379200"
    
    location_id = "us-central1"
   
    agent_id = "d37bd253-e6ab-4041-9442-f31c8f952524"
    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
    
    session_id = str(uuid.uuid4())
    #audio_file_path = "computer_voice_input/Hi.wav"
    audio_file_path = "human_voice/Hi.wav"
    
    language_code = "en-us"

    message = detect_intent_audio(agent, session_id, audio_file_path, language_code)

    language = 'en'

    myobj = gTTS(text=message, lang=language, slow=False)
    out_dir = f'computer_voice_output/message{response_num}.wav'
    myobj.save(out_dir)
    playsound(out_dir)


def detect_intent_audio(agent, session_id, audio_file_path, language_code):
    """Returns the result of detect intent with an audio file as input.
    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session_path = f"{agent}/sessions/{session_id}"
    print(f"Session path: {session_path}\n")
    client_options = None
    agent_components = AgentsClient.parse_agent_path(agent)
    location_id = agent_components["location"]
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    session_client = SessionsClient(client_options=client_options)

    input_audio_config = audio_config.InputAudioConfig(
        audio_encoding=audio_config.AudioEncoding.AUDIO_ENCODING_LINEAR_16,
        sample_rate_hertz=24000,
    )

    with open(audio_file_path, "rb") as audio_file:
        input_audio = audio_file.read()

    audio_input = session.AudioInput(config=input_audio_config, audio=input_audio)
    query_input = session.QueryInput(audio=audio_input, language_code=language_code)
    request = session.DetectIntentRequest(session=session_path, query_input=query_input)
    response = session_client.detect_intent(request=request)

    print("=" * 20)
    print(f"Query text: {response.query_result.transcript}")
    response_messages = [
        " ".join(msg.text.text) for msg in response.query_result.response_messages
    ]
    print(f"Response text: {' '.join(response_messages)}\n")
    return ' '.join(response_messages)


# [END dialogflow_detect_intent_audio]

if __name__ == "__main__":
    run_sample()