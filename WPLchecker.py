#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import signal

def banner():
    print """___       _______________       ______            ______
__ |     / /__  __ \__  / _________  /_______________  /______________
__ | /| / /__  /_/ /_  /  _  ___/_  __ \  _ \  ___/_  //_/  _ \_  ___/
__ |/ |/ / _  ____/_  /___/ /__ _  / / /  __/ /__ _  ,<  /  __/  /
____/|__/  /_/     /_____/\___/ /_/ /_/\___/\___/ /_/|_| \___//_/

+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
+                     [   WPLchecker  v1.0b   ]                     +
+          [   65 Vulnerabilidades   ]  [   57 Plugins   ]          +
+           Escrito por:  Juampa @UnD3sc0n0c1d0 Rodríguez           +
+                 MOEBIUS TEAM - blog.moebiusec.com                 +
+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +"""

def usage():
    print """
    USO: WPLchecker [Objetivo]

    NOTA.- Puedes visualizar la lista completa de plugins pulsando:

    WPLchecker plugins
    """

def scanning():
    if len(sys.argv[0:]) == 1:
        banner()
        usage()
    elif len(sys.argv[0:]) > 2:
        print """
ADVERTENCIA.- No ha ejecutado la herramienta de forma correcta, por favor, revise la ayuda."""
        usage()
    elif sys.argv[1] == "plugins":
        os.system("cat plugins")
        print ""
    elif sys.argv[1] == "paths":
        print """
ADVERTENCIA.- No ha ejecutado la herramienta de forma correcta, por favor, revise la ayuda."""
        usage()
    elif len(sys.argv[0:]) == 2:
        banner()
        VRS1 = os.popen("curl -s " + sys.argv[1] + " | grep 'content=\"WordPress' | cut -d '\"' -f4").read()
        VRS2 = os.popen("curl -s " + sys.argv[1] + "/wp-login.php | grep ';ver=' | cut -d ';' -f4 | cut -d '=' -f2 | cut -d \"'\" -f1 | grep .").read()
        if VRS1 != "":
            VRS3 = VRS1
        else:
            VRS3 = VRS2
        print "\nOBJETIVO: " + sys.argv[1] + " | VERSIÓN: " + VRS3
        print "========================================================================================================================================================================"
        print "Plugins                     Versión   Fabricante                                  Vulnerabilidad                        Readme (site/wp-content/plugins/)"
        print "========================================================================================================================================================================"
        LST=open("paths")
        for PLG in LST:
            PLG = PLG[:-1]
            RST = os.popen("curl -sI " + sys.argv[1] + "/wp-content/plugins/" + PLG + "/readme.txt | grep -c OK").read()
            if int(RST) == 1:
                os.system("cat plugins | grep ' " + PLG + "'")
        print ""

def keyboard_interrupt(signal, frame):
    print('\n')
    sys.exit()
signal.signal(signal.SIGINT, keyboard_interrupt)

scanning()
