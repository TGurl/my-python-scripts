#!/usr/bin/env bash
pyinstaller --onefile blackscreen.py
mv dist/blackscreen ~/.bin/blackscreen
rm -r build
rm -r dist
rm blackscreen.spec
