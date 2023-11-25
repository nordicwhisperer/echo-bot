#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "12b4d4ae-cffc-49f3-bf30-b08b029bbe90")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
