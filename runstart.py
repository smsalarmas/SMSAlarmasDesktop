#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from win32api import (GetModuleFileName, RegCloseKey, RegDeleteValue,
                      RegOpenKeyEx, RegSetValueEx)
from win32con import HKEY_LOCAL_MACHINE, KEY_WRITE, REG_SZ
SUBKEY = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
def run_at_startup_set(appname, path):
    """
    Sets the registry key to run at stratup.
    """
    key = RegOpenKeyEx(HKEY_LOCAL_MACHINE, SUBKEY, 0, KEY_WRITE)
    RegSetValueEx(key, appname, 0, REG_SZ, path)
    RegCloseKey(key)
def run_script_at_startup_set(appname, script):
    path = "%s %s" % (GetModuleFileName(0), script)
    run_at_startup_set(appname, path)
def run_at_startup_remove(appname):
    """
    Removes the run-at-startup registry key.
    """
    key = RegOpenKeyEx(HKEY_LOCAL_MACHINE, SUBKEY, 0, KEY_WRITE)
    RegDeleteValue(key, appname)
    RegCloseKey(key)

if sys.argv[1] == 'add':
    run_at_startup_set(sys.argv[2],sys.argv[3])

elif sys.argv[1] == 'delete':
    run_at_startup_remove(sys.argv[2])

