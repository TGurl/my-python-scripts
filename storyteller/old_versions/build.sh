#!/usr/bin/env bash

# ---- check if the build and dist folders exist
# ---- if so, then delete them
[ -d build ] && rm -r build
[ -d dist ] && rm -r dist
[ -f st.spec ] && rm st.spec

# ---- build the storyteller st binary
pyinstaller --onefile st

# ---- move the binary to ~/.bin/
mv dist/st ~/.bin/

# ---- cleaning up
rm -r build
rm -r dist
rm -r st.spec

clear
echo "'st' has been build and moved to ~/.bin"
