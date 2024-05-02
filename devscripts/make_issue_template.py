#!/usr/bin/env python3

# Allow direct execution
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import re

from devscripts.utils import (
    get_filename_args,
    read_file,
    read_version,
    write_file,
)

VERBOSE_TMPL = '''
  - type: checkboxes
    id: verbose
    attributes:
      label: Provide verbose output that clearly demonstrates the problem
      options:
        - label: Run **your** yt-dlp command with **-vU** flag added (`yt-dlp -vU <your command line>`)
          required: true
        - label: "If using API, add `'verbose': True` to `YoutubeDL` params instead"
          required: false
        - label: Copy the WHOLE output (starting with `[debug] Command-line config`) and insert it below
          required: true
  - type: textarea
    id: log
    attributes:
      label: Complete Verbose Output
      description: |
        It should start like this:
      placeholder: |
        [debug] Command-line config: ['-vU', 'test:youtube']
        [debug] Portable config "yt-dlp.conf": ['-i']
        [debug] Encodings: locale UTF-8, fs utf-8, pref UTF-8, out utf-8 (No ANSI), error utf-8 (No ANSI), screen utf-8 (No ANSI)
        [debug] yt-dlp version stable@2023.10.13 [b634ba742] (source)
        [debug] Lazy loading extractors is disabled
        [debug] Git HEAD: f8abf45
        [debug] LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.6/x64/lib
        [debug] Proxy map: {}
        [debug] Fetching release info: https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest
        Latest version: %(version)s, Current version: %(version)s
        yt-dlp is up to date (%(version)s)
        <more lines>
      render: shell
    validations:
      required: true
'''.strip()

NO_SKIP = '''
  - type: checkboxes
    attributes:
      label: DO NOT REMOVE OR SKIP THE ISSUE TEMPLATE
      description: Fill all fields even if you think it is irrelevant for the issue
      options:
        - label: I understand that I will be **blocked** if I *intentionally* remove or skip any mandatory\\* field
          required: true
'''.strip()


def main():
    fields = {'version': read_version(), 'no_skip': NO_SKIP}
    fields['verbose'] = VERBOSE_TMPL % fields
    fields['verbose_optional'] = re.sub(r'(\n\s+validations:)?\n\s+required: true', '', fields['verbose'])

    infile, outfile = get_filename_args(has_infile=True)
    write_file(outfile, read_file(infile) % fields)


if __name__ == '__main__':
    main()
