from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk.events import SlotSet, Form
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
import requests
import json
class ExistingUserForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "existing_user_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["phone", "dob"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "phone": [
                self.from_text(),
            ],
            "dob": [
                self.from_text(),
            ],
        }
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        """Define what the form has to do
            after all required slots are filled"""

        vMobileNos = tracker.get_slot('phone')
        vDobs = tracker.get_slot('dob')
        
        # dispatcher.utter_message(vMobileNos)
        # dispatcher.utter_message(vDobs)
    
        # r = PyQuery.getJSON('http://115.127.24.183/leadschatbotgateway/api/userinfo/getuserinfo?vMobileNo='+vMobileNos+'&vDob='+vDobs)
        r = requests.get('http://115.127.24.183/leadschatbotgateway/api/userinfo/getuserinfo?vMobileNo='+vMobileNos+'&vDob='+vDobs)
        response = r.text
        # response = r.json()
        # response = json.loads(data)
        # dispatcher.utter_message(r)
    
        # dispatcher.utter_message("Thanks for entering data")
        if response == '[]':
            dispatcher.utter_message('Your mobile number or date of birth is incorrect')
        elif response != None:
            dispatcher.utter_message(response)
        return []



# class ActionUtterAndSetSlot(FormAction):
#     def name(self):
#         return "form_set_slot"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         return ["response"]

    

#     def run(self, dispatcher, tracker, domain):
#         message = (tracker.latest_message)['text']
#         print("why? ",message)
#         return [SlotSet('response', message)]
