## greet
* chitchat/greet
    - 初次见面，请多关照
## goodbye
* chitchat/goodbye
    - 好的，下次再见
## thanks
* chitchat/thanks
    - 能帮到你就好   
## praise
* chitchat/praise
    - 哈哈，很感谢
## ask weather    
* utter_ask_LOCATION:
    - text: 你是想问哪里的天气？
* utter_ask_DATE:
-   - text: 你是想问明天还是后天的天气？
* utter_ask_confirm_ask:
    - text: "你是确定要问天气吗？"  
      buttons:
      - title: "是的"
        payload: '/affarm{"CONFIRM_ASK": "True"}'
      - title: "不需要"
        payload: '/deny{"CONFIRM_ASK": "False"}'
* utter_slots_values:
      - text: "你是想问:{LOCATION}的{DATE}天气吗？"
    