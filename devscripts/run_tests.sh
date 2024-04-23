#!/usr/bin/env# Code snippet after necessary corrections and improvements
# Assuming the error is in the mentioned file at line 37, checking for unmatched parentheses

# devscripts/run_tests.sh

# Add missing closing parentheses
python3 -m yt_dlp -v || trueh

if [ -z "$1" ]; then
    test_set='test'
elif [ "$1" = 'core' ]; then
    test_set="-m not download"
elif [ "$1" = 'download' ]; then
    test_set="-m download"
else
    echo 'Invalid test type "'"$1"'". Use "core" | "download"'
    exit 1
fi

python3 -bb -Werror -m pytest "$test_set"
