#!/usr/bin/env python

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
DialogFlow API Detect Intent Python sample with text inputs.
"""
#export GOOGLE_APPLICATION_CREDENTIALS=“/home/<your-user>/credentials/google_dialogflow_api.json”
import argparse
import uuid
import json

from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3beta1.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3beta1.types import session
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
from playsound import playsound

class DialogFlowAgent():
        
    def __init__(self):   
        #f"projects/{self.project_id}/locations/{self.location_id}/agents/{self.agent_id}"        
        #google_cloud_agent_path = "projects/final-picnic-with-some-peanuts/locations/us-central1/agents/0dd93541-aa75-4457-a5c8-fd04474140fe"
        google_cloud_agent_path = "projects/yilin-test-379200/locations/us-central1/agents/d37bd253-e6ab-4041-9442-f31c8f952524"
        # For more information on sessions see https://cloud.google.com/dialogflow/cx/docs/concept/session
        self.create_session(google_cloud_agent_path)
        

    def create_session(self, agent):
        """Returns the result of detect intent with texts as inputs.
        Using the same `session_id` between requests allows continuation
        of the conversation."""

        session_id = uuid.uuid4()
        self.session_path = f"{agent}/sessions/{session_id}"
        print(f"Session path: {self.session_path}\n")

        client_options = None
        agent_components = AgentsClient.parse_agent_path(agent)
        location_id = agent_components["location"]
        if location_id != "global":
            api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
            print(f"API Endpoint: {api_endpoint}\n")
            client_options = {"api_endpoint": api_endpoint}
        self.session_client = SessionsClient(client_options=client_options)

    def send_utterance(self, text, language_code="es"):
        """
        """
        text_input = session.TextInput(text=text)
        query_input = session.QueryInput(text=text_input, language_code=language_code)
        request = session.DetectIntentRequest(session=self.session_path, query_input=query_input)
        response = self.session_client.detect_intent(request=request)
        response_mesg = [ txt for msg in response.query_result.response_messages for txt in msg.text.text ]
        response_mesg = response_mesg[0]
        # print('‣ Response Id: ', response.response_id)
        # print('‣ Match: ', response.query_result.match)
        # print('‣ Parameters: ', response.query_result.parameters)

        print('‣ response: ',response_mesg)
        return response_mesg


if __name__ == "__main__":
    ag = DialogFlowAgent()

    text = 'Hi'
    print('‣ input: ',text)
    full_response = ag.send_utterance(text)
    # language = 'en'
    # myobj = gTTS(text=full_response, lang=language, slow=False)

    # myobj.save("temp.mp3")

    # playsound("temp.mp3")

    # text = 'this book'
    # print('‣ input: ',text)
    # full_response = ag.send_utterance(text)
    # # myobj = gTTS(text=full_response, lang=language, slow=False)

    # # myobj.save("temp.mp3")

    # # playsound("temp.mp3")

    # text = 'hi'
    # print('‣ input: ',text)
    # full_response = ag.send_utterance(text)


    # text = 'benjamin'
    # print('‣ input: ',text)
    # full_response = ag.send_utterance(text)
    # # myobj = gTTS(text=full_response, lang=language, slow=False)

    # # myobj.save("temp.mp3")

    # # playsound("temp.mp3")

    # text = 'lucy'
    # print('‣ input: ',text)
    # full_response = ag.send_utterance(text)
    # text = 'bear'
    # print('‣ input: ',text)
    # full_response = ag.send_utterance(text)
    # text = 'Hi'
    # print('‣ input: ',text)
    # full_response = ag.send_utterance(text)


    