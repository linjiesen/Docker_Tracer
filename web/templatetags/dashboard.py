# -*-coding:utf-8-*-

from django.template import Library
from django.urls import reverse

from web import models

register = Library()


@register.simple_tag
def user_space(size):
    """
    设置显示前端文件大小格式化
    使用方法： html页面调用{% load dashboard %}
    在使用的地方格式如下
                            {% if item.file_type == 1 %}
                                {% user_space item.file_size %}
                                {# {{ item.file_size }}#}
                            {% else %}
                                -
                            {% endif %}

    """
    if size >= 1024 * 1024 * 1024:
        return "%.2f GB" % (size / (1024 * 1024 * 1024))
    elif size >= 1024 * 1024:
        return "%.2f MB" % (size / (1024 * 1024))
    elif size >= 1024:
        return "%.2f KB" % (size / 1024)
    else:
        return "%.2f B" % size



