# -*- coding:utf-8 -*-
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from BugManage.local_settings import *


def send_sms_single(phone_num, template_id, template_param_list):
    """
    單條發送短信
    :param phone_num: 手機號
    :param template_id:騰訊雲短信模板ID
    :param template_param_list:短信模板所需參數列表，例如：[驗證碼：{1}, 描述：{2}],則傳遞 參數[888, 666]按順尋去格式化模板
    :return:
    """
    appid = TENCENT_SMS_APP_ID
    appkey = TENCENT_SMS_APP_KEY
    sms_sign = TENCENT_SMS_SIGN

    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "網絡異常發送失敗 "}
    return response


def send_sms_multi(phone_num_list, template_id, param_list):
    """
    批量發送短信
    :param phone_num:手機號
    :param template_id:騰訊雲短信模板ID
    :param param_list:短信模板所需參數列表，例如：[驗證碼：{1}, 描述：{2}],則傳遞 參數[888, 666]按順尋去格式化模板
    :return:
    """
    appid = TENCENT_SMS_APP_ID
    appkey = TENCENT_SMS_APP_KEY
    sms_sign = TENCENT_SMS_SIGN

    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "網絡異常發送失敗 "}
    return response
