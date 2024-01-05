#!/usr/bin/env bash
pyinstaller --onefile st.py
mv dist/st ~/.bin/st
rm -r build
rm -r dist
rm st.spec
