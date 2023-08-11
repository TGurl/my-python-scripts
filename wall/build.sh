#!/usr/bin/env bash

[ -d dist ] && rm -r dist
[ -d build ] && rm -r build
[ -f wp.spec ] && rm wp.spec

pyinstaller --onefile wp.py
mv dist/wp ~/.bin/

rm -r dist
rm -r build
rm wp.spec
