#!/usr/bin/env bash
pyinstaller --onefile cia.py
mv dist/cia ~/.bin/cia
rm -r build
rm -r dist
rm cia.spec
