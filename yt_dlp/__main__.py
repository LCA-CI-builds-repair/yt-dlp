#!/usr/bin/env python3
import importlib.util

spec = importlib.util.find_spec('sportsbettingapi.sites.elevensports_ie')
ElevenSportsIE = spec.loader.load_module()

from sportsbettingapi.sites.elevensports_ie import ElevenSportsIE

if __name__ == "__main__":
    # Your main code here