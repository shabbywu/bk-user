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
from typing import Dict

import bkuser_sdk
from bkuser_sdk.configuration import Configuration
from django.conf import settings

client_configuration = Configuration()

if settings.BK_USER_CORE_API_HOST:
    client_configuration.host = settings.BK_USER_CORE_API_HOST


def get_api_client(default_headers: Dict = None) -> bkuser_sdk.ApiClient:
    """获得一个 api client"""
    default_headers = default_headers or {}
    api_client = bkuser_sdk.ApiClient(client_configuration)

    for header_name, header_value in default_headers.items():
        api_client.set_default_header(header_name=header_name, header_value=header_value)

    return api_client
