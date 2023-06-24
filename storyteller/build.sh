#!/usr/bin/env bash

pyinstaller --onefile st.py

mv dist/st ~/.bin

rm -r dist
rm -r build
rm st.spec
