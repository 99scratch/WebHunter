#!/usr/bin/env python
# WebHunter MiniModule

import re


class Hyperguard:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'^WODSESSION=', item[1], re.I) is not None
            if w:
                return "Hyperguard Web Application Firewall (art of defence)"
                break
