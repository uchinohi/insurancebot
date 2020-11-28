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
from .options import Option


class ActionCheckOtp(Action):

    def name(self) -> Text:
        return "action_check_otp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        otp = tracker.get_slot('otp')

        otp_list = ['1234','6789','4585','9669']

        def get_started(num):
            name = Query.return_name(num)
            start_message = f'Welcome {name}!\nWhat help do you need today?\n1. Calculate Premium\t2. Claims Query\n3. Renewal Query\t4. My Policy\n5. Search Network Hospitals\t6. Download Claim Forms\n\nPress required number to get started.'
            dispatcher.utter_message(start_message)

        if otp in otp_list:
            dispatcher.utter_message(template='utter_verified')
            get_started(tracker.get_slot('mobile_number'))
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

class ActionExecuteOption(Action):

    def name(self) -> Text:
        return "action_execute_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        opt = str(next(tracker.get_latest_entity_values('option_select'), None))
        num = tracker.get_slot('mobile_number')

        opobj = Option(opt,num)

        message = opobj.executeOption()

        dispatcher.utter_message(message)


        return []


class ActionClaimStatus(Action):

    def name(self) -> Text:
        return "action_claim_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # opt = str(next(tracker.get_latest_entity_values('option_select'), None))
        claimno = tracker.get_slot('claim_no')
        num = tracker.get_slot('mobile_number')



        message = Query.return_claim_status(num,claimno)

        dispatcher.utter_message(message)


        return []


