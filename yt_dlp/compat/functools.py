from .compat_utils import passthrough_module

passthrough_module(__name__, 'functools')
del passthrough_module

try:
    from functools import cache  # >= 3.9
except NameError:
    from functools import lru_cache
    cache = lru_cache(maxsize=None)