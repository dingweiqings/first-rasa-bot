# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
import datetime

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="抱歉,您可以再重复一遍吗？")
        return [UserUtteranceReverted()]
class ActionShowNow(Action):

    def name(self) -> Text:
        return "action_show_now"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time=datetime.datetime.now().strptime("%Y-%m-%d %H:%M:%S")
        dispatcher.utter_message(text="现在是"+time)
        return [UserUtteranceReverted()]
class ActionAskWather(Action):

    def name(self) -> Text:
        return "action_ask_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        weather="天气晴，温度40度"
        dispatcher.utter_message(text=""+weather)
        return [UserUtteranceReverted()]