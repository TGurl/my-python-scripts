#!/usr/bin/env bash
pyinstaller --onefile zipr.py
mv dist/zipr ~/.bin/zipr
rm -r build
rm -r dist
rm zipr.spec
