## intent:chitchat/greet
- 你好
- 你好啊
- 初次见面
- 你好，有什么可以帮您吗
- 你是谁

## intent:affirm
- 是的
- 确实
- 必须的
- 好的
- 很好
- 嗯嗯
- 很对
- 很棒
- good
- 对对
- 对对对
## intent:deny
- 不需要
- 不
- 不用
- 不用，谢谢
## intent:chitchat/goodbye
- 我先走了
- 拜拜
- 88
- 白白
## intent:inform
- [苏州](LOCATION)
- 我想知道[今天](DATE)[苏州](LOCATION)的天气
- [今天](DATE)天气是晴
## intent:chitchat/thanks
- 谢谢
- 谢谢你

## intent:inform
- 大概 [8 小时](TIME)

## intent:out_of_scope
- 这些我做不了
- 等等
- 我帮不了你
- 对不起这些我不会
## intent:help
- 需要帮忙

## intent:special_bussiness
- 我想订个票

## intent:chitchat/praise
- 真好

## intent:ask_weather
- [今天](DATE)天气怎么样
- 我想知道[今天](DATE)天气
- 我[今天](DATE)需要带伞吗
- [今天](DATE)天气
- [今天](DATE)是晴天吗
- [今天](DATE)天气是什么
## intent:ask_now
- [现在](TIME)到5点半了吗
- 还有几分钟到10点
- [现在](TIME)什么时间了
- 现在几点
- 几点了
- 什么时间了

## regex:greet_regex
- ^你好[啊|呀]*$

## regex:must_situation
- \\w+必须\\w+
