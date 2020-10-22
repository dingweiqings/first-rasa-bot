from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionAskWeather(FormAction):

    def name(self):
        return "weather_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        if tracker.get_slot('CONFIRM_ASK') == True:
            return ["LOCATION"]
        else:
            return ["DATE","LOCATION"]

    async def submit(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[
        EventType]:
            dispatcher.utter_message("谢谢，明天是xxx")
            return []
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "CONFIRM_ASK": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],
            "LOCATION": [
                self.from_entity(entity="LOCATION"),
                self.from_intent(intent="deny", value="None"),
            ],
            "DATE": [
                self.from_entity(entity="DATE"),
                self.from_intent(intent="deny", value="None"),
            ]

        }
