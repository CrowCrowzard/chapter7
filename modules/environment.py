#!/usr/bin/env python
# coding: UTF-8

import os

def run(**args):
    print "[*] In environment module."
    return str(os.environ)

