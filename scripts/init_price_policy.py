#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scripts import base
from web import models


def run():
    exists = models.PricePolicy.objects.filter(category=1, title="个人免费版").exists()
    if not exists:
        result = models.PricePolicy.objects.create(
            category=1,
            title="个人免费版",
            price=0,
            project_num=5,
            project_member=2,
            project_space=20,
            per_file_size=20,
        )
        print(result)



if __name__ == '__main__':
    run()
