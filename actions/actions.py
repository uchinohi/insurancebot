# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .database import Query


class ActionCheckOtp(Action):

    def name(self) -> Text:
        return "action_check_otp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        otp = tracker.get_slot('otp')

        otp_list = ['1234','6789','4585']

        if otp in otp_list:
            dispatcher.utter_message(template='utter_verified')
        else:
            dispatcher.utter_message(template='utter_wrong')

        return []

class ActionCheckNumber(Action):

    def name(self) -> Text:
        return "action_check_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        num = tracker.get_slot('mobile_number')

        flag = Query.search_mobile(num)

        if flag:
            dispatcher.utter_message(template='utter_enter_otp')
        else:
            dispatcher.utter_message(template='utter_sign_up')

        return []
