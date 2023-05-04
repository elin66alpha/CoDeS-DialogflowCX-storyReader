
import uuid
import os
from google.cloud.dialogflowcx_v3.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3.types import audio_config
from google.cloud.dialogflowcx_v3.types import session

from google.oauth2.service_account import Credentials

import pyaudio
import wave
from gtts import gTTS
import winplaysound


class flow:
    agent = ''
    session_id = ''
    language_code = "en-us"
    location_id = "us-central1"
    audio_filename = ''
    book = ''
    read = ''
    user_name = ''
    question = 0
    answer = 0
    block_signal = False
    seconds = 4
    key_exist = False
    NQ_flag = False



    def setBook_Read(self,book,read):
        self.block_signal = False
        self.book = book
        self.read = read
        self.answer = 0
        self.question = 0
        print(book,read,self.NQ_flag)
        self.init()
        
    def setNQ(self,flag):
        self.NQ_flag = flag


    def init(self):
        try:
            os.mkdir('human_voice_input')
        except:
            pass
        try:
            os.mkdir('computer_voice_output')
        except:
            pass
        if(self.book == 'picnic' and self.NQ_flag == False):
            try:
                self.Credential = Credentials.from_service_account_file("keys/picnic_key.json")
            except:
                print("no key found")
                self.key_exist = False
                return
            self.key_exist = True
            project_id = "final-picnic-with-some-peanuts"
            if(self.read == 1):
                agent_id = "0dd93541-aa75-4457-a5c8-fd04474140fe"
            elif(self.read == 2):
                agent_id = "758c0020-58ff-45bd-9b1d-48e799c55dfe"
            elif(self.read == 3):
                agent_id = "ae1a91bb-a38a-4d45-827a-530e44910c0c"
        elif(self.book == 'picnic' and self.NQ_flag == True):
            try:
                self.Credential = Credentials.from_service_account_file("keys/picnic_key.json")
            except:
                print("no key found")
                self.key_exist = False
                return
            self.key_exist = True
            project_id = "final-picnic-with-some-peanuts"
            if(self.read == 1):
                agent_id = "a95e2230-678f-48f7-857e-3309bee06f97"
            elif(self.read == 2):
                agent_id = "a6ea0f8a-d65e-481d-8249-01c4c01df4d1"
            elif(self.read == 3):
                agent_id = "b31218dc-7483-45fd-ae98-e45ea36c8d93"
        elif(self.book == 'maria'):
            try:
                self.Credential = Credentials.from_service_account_file("keys/maria_key.json")
            except:
                print("no key found")
                self.key_exist = False
                return
            self.key_exist = True
            project_id = "final-marias-perfect-day"
            if(self.read == 1):
                agent_id = "db2a4961-593c-4b46-9237-a406ba48946b"
            elif(self.read == 2):
                agent_id = "a77156b2-73a0-403a-b60a-e610aec291de"
            elif(self.read == 3):
                agent_id = "1ffea9ee-aba0-4ffd-985a-45248a0a0223"
        elif(self.book == 'train'):
            try:
                self.Credential = Credentials.from_service_account_file("keys/yilin_key.json")
            except:
                print("no key found")
                self.key_exist = False
                return
            self.key_exist = True
            project_id = "yilin-test-379200"
            agent_id = "d37bd253-e6ab-4041-9442-f31c8f952524"
        
        self.agent = f"projects/{project_id}/locations/{self.location_id}/agents/{agent_id}"
        self.session_id = str(uuid.uuid4())

    def update_name_time(self,name,second):
        self.user_name = name
        if(second != ''):
            if(int(second) > 10):
                self.seconds = 10
            elif(int(second) < 1):
                self.seconds = 4
            else:
                self.seconds = int(second)
        else:
            self.seconds = 4
            
    def send_audio(self, text):
        if (self.check_init()):
            message = self.detect_intent_audio(text)
            if(message != ''):
                language = 'en'
                myobj = gTTS(text=message, lang=language, slow=False)
                self.question += 1
                out_dir = f'computer_voice_output/feedback,{self.book}{self.read},{self.user_name}{self.question}.mp3'
                myobj.save(out_dir)
                self.block_signal = True
                winplaysound.playsound(out_dir)
                self.block_signal = False
            else:
                print("no message received")
        else:
            print("can't send your request, please select a book and readding! or check your internet connection and key file")

    def detect_intent_audio(self,text):
        """Returns the result of detect intent with an audio file as input.
        Using the same `session_id` between requests allows continuation
        of the conversation."""
        session_path = f"{self.agent}/sessions/{self.session_id}"
        print(f"Session path: {session_path}\n")
        client_options = None
        agent_components = AgentsClient.parse_agent_path(self.agent)
        location_id = agent_components["location"]
        if location_id != "global":
            api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        session_client = SessionsClient(credentials = self.Credential,client_options=client_options) #choose the creds
        if(text):
            text_input = session.TextInput(text=text)
            query_input = session.QueryInput(text=text_input, language_code=self.language_code)
        else:
            input_audio_config = audio_config.InputAudioConfig(
                audio_encoding=audio_config.AudioEncoding.AUDIO_ENCODING_LINEAR_16,
                sample_rate_hertz=24000,)
            with open(self.audio_filename, "rb") as audio_file:
                input_audio = audio_file.read()
            audio_input = session.AudioInput(config=input_audio_config, audio=input_audio)
            query_input = session.QueryInput(audio=audio_input, language_code=self.language_code)

        request = session.DetectIntentRequest(session=session_path, query_input=query_input)
        response = session_client.detect_intent(request=request)

        print("=" * 20)
        print(f"Query text: {response.query_result.transcript}")
        response_messages = [
            " ".join(msg.text.text) for msg in response.query_result.response_messages
        ]
        print(f"Response text: {' '.join(response_messages)}\n")
        return ' '.join(response_messages)



    def record(self):

        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 1
        fs = 24000 # Record at 44100 samples per second
        self.answer += 1
        filename = f'human_voice_input/record,{self.book}{self.read},{self.user_name}{self.answer}.wav'
        self.audio_filename = filename
        p = pyaudio.PyAudio()  # Create an interface to PortAudio

        print('Recording')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        for i in range(0, int(fs / chunk * self.seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream 
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        # Save the recorded data as a WAV file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        self.send_audio(None)
    
    def check_init(self):
        complete_init_flag = False
        if(self.book != '' and self.read != '' and self.block_signal == False and self.key_exist == True):
            complete_init_flag = True
        return complete_init_flag



# # example of manual test
# if __name__ == '__main__':
#     flow = flow() # create a flow object

#     # set the book and read
#     flow.setBook_Read('yilin',3) 
#     flow.send_audio('hello')
#     #switch to another book
#     flow.setBook_Read('picnic',2)
#     flow.send_audio('hello')
#     #switch to another book
#     flow.setBook_Read('maria',1)
#     flow.send_audio('hello')
