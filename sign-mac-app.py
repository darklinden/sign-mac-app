#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def main():

    # codesign --force --verify --verbose --sign "Mac Developer"

    app_path = ''
    if len(sys.argv) > 1:
        app_path = sys.argv[1]

    if len(app_path) == 0:
        print("using sign-mac-app.py [app-path] to sign app")
        return -1

    if not os.path.isabs(app_path):
        app_path = os.path.join(os.getcwd(), app_path)

    app_path = app_path.rstrip('/')

    if not (os.path.isdir(app_path) and str(app_path).lower().endswith('.app')):
        print("using sign-mac-app.py [app-path] to sign app")
        return -1

    print("remove attr: " + app_path)
    os.system('xattr -cr "' + app_path + '"')

    print("codesign: " + app_path)
    os.system('codesign --force --verify --verbose --sign "Mac Developer" "' + app_path + '"')

    for root, dirs, files in os.walk(app_path):
        sub_files = os.listdir(root)
        for fn in sub_files:
            file_path = root + "/" + fn
            if os.path.isfile(file_path):
                print("codesign: " + file_path)
                os.system('codesign --force --verify --verbose --sign "Mac Developer" "' + file_path + '"')

    print("Done")


if __name__ == '__main__':
    main()
