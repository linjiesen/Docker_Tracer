# -*-coding:utf-8 -*-
import os

LANGUAGE_CODE = 'zh-hans'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 配置文件Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8'
            },
            'SOCKER_TIMEOUT': 10,
            'PASSWORD': "123456",
        }
    }
}

# # 騰訊雲短信應用的app_id
# TENCENT_SMS_APP_ID = 1400369143
# # 騰訊雲短信應用的 app_key
# TENCENT_SMS_APP_KEY = "84418dd98abd7cf42107dedb4093c3b8"
# # 騰訊雲短信籤名內容
# TENCENT_SMS_SIGN = "代碼and詩"
#
# TENCENT_SMS_TEMPLATE = {
#     'register': 641424,
#     'login': 641422,
# }
#
# # 腾讯COS的ID和KEY
# TENCENT_COS_ID = "AKIDylQ6XiKBFBuT7epJtFOK4whFZQ2NoI9j"
# TENCENT_COS_KEY = "hAPTIr9WeV6XjfLlCNK0Wnoc9vXu2rRu"
#
#
# ALI_GATEWAY = "https://openapi.alipaydev.com/gateway.do"
# ALI_PRI_KEY_PATH = os.path.join(BASE_DIR, 'files/私钥.txt')
# ALI_PUB_KEY_PATH = os.path.join(BASE_DIR, 'files/支付宝公钥.txt')
# ALI_NOTIFY_URL = "http://127.0.0.1:8000/pay/notify"
# ALI_RETURN_URL = "http://127.0.0.1:8000/pay/notify"
# ALI_APPID = "2021000117637762"

