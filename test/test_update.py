#!/usr/bin/env python3

# Allow direct execution
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from test.helper import FakeYDL, report_warning
from yt_dlp.update import Updater, UpdateInfo

TEST_API_DATA = {
    'yt-dlp/yt-dlp/latest': {
        'tag_name': '2023.12.31',
        'target_commitish': 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
        'name': 'yt-dlp 2023.12.31',
        'body': 'BODY',
    },
    'yt-dlp/yt-dlp-nightly-builds/latest': {
        'tag_name': '2023.12.31.123456',
        'target_commitish': 'master',
        'name': 'yt-dlp nightly 2023.12.31.123456',
        'body': 'Generated from: https://github.com/yt-dlp/yt-dlp/commit/cccccccccccccccccccccccccccccccccccccccc',
    },
    'yt-dlp/yt-dlp-master-builds/latest': {
        'tag_name': '2023.12.31.987654',
        'target_commitish': 'master',
        'name': 'yt-dlp master 2023.12.31.987654',
        'body': 'Generated from: https://github.com/yt-dlp/yt-dlp/commit/dddddddddddddddddddddddddddddddddddddddd',
    },
    'yt-dlp/yt-dlp/tags/testing': {
        'tag_name': 'testing',
        'target_commitish': '9999999999999999999999999999999999999999',
        'name': 'testing',
        'body': 'BODY',
    },
    'fork/yt-dlp/latest': {
        'tag_name': '2050.12.31',
        'target_commitish': 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
        'name': '2050.12.31',
        'body': 'BODY',
    },
    'fork/yt-dlp/tags/pr0000': {
        'tag_name': 'pr0000',
        'target_commitish': 'ffffffffffffffffffffffffffffffffffffffff',
        'name': 'pr1234 2023.11.11.000000',
        'body': 'BODY',
    },
    'fork/yt-dlp/tags/pr1234': {
        'tag_name': 'pr1234',
        'target_commitish': '0000000000000000000000000000000000000000',
        'name': 'pr1234 2023.12.31.555555',
        'body': 'BODY',
    },
    'fork/yt-dlp/tags/pr9999': {
        'tag_name': 'pr9999',
        'target_commitish': '1111111111111111111111111111111111111111',
        'name': 'pr9999',
        'body': 'BODY',
    },
    'fork/yt-dlp-satellite/tags/pr987': {
        'tag_name': 'pr987',
        'target_commitish': 'master',
        'name': 'pr987',
        'body': 'Generated from: https://github.com/yt-dlp/yt-dlp/commit/2222222222222222222222222222222222222222',
    },
}

TEST_LOCKFILE_COMMENT = '# This file is used for regulating self-update'

TEST_LOCKFILE_V1 = r'''%s
lock 2022.08.18.36 .+ Python 3\.6
lock 2023.11.16 (?!win_x86_exe).+ Python 3\.7
lock 2023.11.16 win_x86_exe .+ Windows-(?:Vista|2008Server)
''' % TEST_LOCKFILE_COMMENT

TEST_LOCKFILE_V2_TMPL = r'''%s
lockV2 yt-dlp/yt-dlp 2022.08.18.36 .+ Python 3\.6
lockV2 yt-dlp/yt-dlp 2023.11.16 (?!win_x86_exe).+ Python 3\.7
lockV2 yt-dlp/yt-dlp 2023.11.16 win_x86_exe .+ Windows-(?:Vista|2008Server)
lockV2 yt-dlp/yt-dlp-nightly-builds 2023.11.15.232826 (?!win_x86_exe).+ Python 3\.7
lockV2 yt-dlp/yt-dlp-nightly-builds 2023.11.15.232826 win_x86_exe .+ Windows-(?:Vista|2008Server)
lockV2 yt-dlp/yt-dlp-master-builds 2023.11.15.232812 (?!win_x86_exe).+ Python 3\.7
lockV2 yt-dlp/yt-dlp-master-builds 2023.11.15.232812 win_x86_exe .+ Windows-(?:Vista|2008Server)
'''

TEST_LOCKFILE_V2 = TEST_LOCKFILE_V2_TMPL % TEST_LOCKFILE_COMMENT

TEST_LOCKFILE_ACTUAL = TEST_LOCKFILE_V2_TMPL % TEST_LOCKFILE_V1.rstrip('\n')

TEST_LOCKFILE_FORK = r'''%s# Test if a fork blocks updates to non-numeric tags
# No syntax errors found in the provided code snippet.