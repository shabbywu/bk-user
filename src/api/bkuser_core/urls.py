# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-用户管理(Bk-User) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import logging

from bkuser_core.common.serializers import patch_datetime_field
from django.conf import settings
from django.conf.urls import include, url
from django.utils.module_loading import import_module

patch_datetime_field()


logger = logging.getLogger(__name__)


urlpatterns = []
# 尝试从 INSTALLED_APPS 中动态加载 urls 模块，
# 插件开发时去掉各模块 urls 不影响项目运行
for app in settings.INSTALLED_APPS:
    if not app.startswith("bkuser_core."):
        continue

    try:
        urls_module = f"{app}.urls"
        import_module(urls_module)
        urlpatterns.append(url(r"^", include(urls_module)))
    except ImportError:
        logger.exception("failed to load urls from installed app: %s", app)
        continue


if "silk" in settings.INSTALLED_APPS:
    urlpatterns += [url(r"^silk/", include("silk.urls", namespace="silk"))]
