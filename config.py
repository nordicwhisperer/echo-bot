#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "4c7662b6-35dd-4329-af86-2172c58ea894")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
