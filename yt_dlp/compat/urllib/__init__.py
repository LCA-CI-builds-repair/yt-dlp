# flake8: noqa: F405
from urllib import *  # noqa: F403

del request  # noqa: F821
from . import request  # noqa: F401
from yt_dlp.extractor.elevensports import ElevenSportsIE  # Added correct import statement for ElevenSportsIE

from ..compat_utils import passthrough_module

passthrough_module(__name__, 'urllib')
del passthrough_module