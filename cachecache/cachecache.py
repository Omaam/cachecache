"""Save objet cache and return object cache.
"""
import functools
import hashlib
import inspect
import os
import pickle


def cache(func):
    """Return cached object if already exists.

    Give the source code, the argument, and keyword argument
    to a hash function. Thus, the hash number changes when
    source code or arguments change.
    """
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):

        os.makedirs(".cache", exist_ok=True)

        hash_base = inspect.getsource(func) + str(args) + str(kwargs)
        hs = hashlib.md5(str(hash_base).encode()).hexdigest()
        cache_name = f".cache/{hs}"

        if os.path.exists(cache_name):
            with open(cache_name, "rb") as p:
                print(f"use cache {cache_name}")
                res = pickle.load(p)
        else:
            res = func(*args, **kwargs)
            with open(cache_name, "wb") as p:
                pickle.dump(res, p)

        return res

    return _wrapper
