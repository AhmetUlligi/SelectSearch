#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser
while True:
    select=input("GOOGLE(G) YANDEX(Y):")

    if select=="G" or select=="g":
        search = input("Search:")
        webbrowser.open("https://www.google.com/search?q=" + search)
    elif select=="Y" or select=="y":
        search1 = input("Search:")
        webbrowser.open("https://yandex.com/search/?lr=11503&text=" + search1)
    else:
        input("TRY AGAIN")






