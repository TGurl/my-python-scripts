#!/usr/bin/env bash

[ -f ~/.bin/wp ] && rm ~/.bin/wp
[ -f wp.spec ] && rm wp.spec
[ -d build ] && rm -r build

pyinstaller --onefile wp.py

mv dist/wp ~/.bin/
echo 'wp moved to ~/.bin'
rm -r dist
rm -r build
rm wp.spec
