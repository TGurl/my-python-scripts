#!/usr/bin/env bash
pyinstaller --onefile arc.py
mv dist/arc ~/.bin/arc
rm -r build
rm -r dist
rm arc.spec
