from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
import datetime

class ActionShowNow(Action):

    def name(self) -> Text:
        return "action_show_now"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dispatcher.utter_message(text="现在是"+time)
        return [UserUtteranceReverted()]
