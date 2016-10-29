#! /usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'dahv'


import sys


def getPlatform():
    platform=''
    if sys.platform.startswith('win'):
        myplatform = 'win'
    elif sys.platform.startwith('linux'):
        myplatform = 'linux'
    return myplatform


