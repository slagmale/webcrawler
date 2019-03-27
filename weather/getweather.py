#! /usr/bin/python
import requests
import json
from wxpy import *
from threading import Timer

def get_weather_json():
    url = 'http://t.weather.sojson.com/api/weather/city/101210101'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }
    # 请求web api拿到数据
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    weather = json.loads(resp.text)
    return weather


# 解析Josn得到需要的数据
def parse_weather_json(weather):
    time = weather['time']  # 该API请求的数据更新时间
    city = weather['cityInfo']['city']  # 城市
    shidu = weather['data']['shidu']  # 湿度
    pm25 = weather['data']['pm25']  # pm2.5
    pm10 = weather['data']['pm10']  # pm10
    quality = weather['data']['quality']  # 空气质量
    wendu = weather['data']['wendu']  # 温度
    forecast = weather['data']['forecast']  # 预测数据  列表类型
    today = forecast[0]
    today_ymd = today['ymd']  # 年月日
    today_week = today['week']  # 星期
    today_high = today['high']  # 最高温度
    today_low = today['low']  # 最低温度
    today_fx = today['fx']  # 风向
    today_fl = today['fl']  # 风力
    today_type = today['type']  # 天气
    today_notice = today['notice']
    tommorrow = forecast[1]

    # 今日天气预报
    result = '今日天气预报:' + '\n' + today_ymd + ' ' + today_week + ' ' + city + '\n' \
             + '风:' + today_fx + ' ' + today_fl + ' ' + '\n' \
             + '温度范围:' + today_low + '~' + today_high + '\n' \
             + 'pm2.5:' + str(pm25) + ' ' + 'pm10:' + str(pm10) + ' ' + '\n' \
             + '空气质量:' + quality + '\n' \
             + '当前温度:' + wendu + '\n' \
             + '湿度:' + shidu + '\n' \
             + '天气:' + today_type + '\n' \
            + '温馨提醒:' + today_notice
    return result


# 发送天气预报
def send_weather(weather_json):

    try:
        result = parse_weather_json(weather_json)
        # 填写微信昵称
        ckz = bot.friends.search(u'CK719')[0]
        ckz.send(u"你好呀Y(^o^)Y，这里是今日份的天气信息请查收!")
        ckz.send(result)
        ckz.send(u'Have a nice day!')
        bot.file_helper.send(result)

        # 每隔86400秒（1天），发送1次
        #t = Timer(86400, send_weather)
        #t.start()
    except:
        #myfriend = bot.friends().search(u'Slagmale')[0]
        #myfriend.send(u"天气预报发送失败！")
        print('失败')
        pass


if __name__ == '__main__':
    weather_json = get_weather_json()
    # 初始化机器人 扫码登陆微信
    bot = Bot(cache_path=True)
    send_weather(weather_json)

