## story_03248462
* chitchat
    - respond_chitchat
## story_help
* help    
   - utter_help
## ask weather happy path
* chitchat
    - respond_chitchat
* ask_weather
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}
* chitchat
    - respond_chitchat
## no ask weather
* chitchat
    - respond_chitchat
* deny
    - utter_goodbye    
## ask weather unhappy path stop
* chitchat
    - respond_chitchat
* ask_weather
    - weather_form
    - form{"name": "weather_form"}
* out_of_scope
    - utter_cheer_up
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye    
## ask weather unhappy path continue
* chitchat
    - respond_chitchat
* ask_weather
    - weather_form
    - form{"name": "weather_form"}
* out_of_scope
    - utter_cheer_up
* affirm
    - weather_form
    - form{"name": null}