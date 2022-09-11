# cachecache
Save objet cache and return object cache.

# Usage
It's easy. Just wrap cache decorator on your function like [`functool.cache`](https://docs.python.org/3/library/functools.html).

```python
import cachecache

@cachecache.cache
def myfunction():
    ret = do_something()
    return ret
```

This will make `.cache` folder and create binary object in this.
The wrapper uses source code, arguments, and keyword arguments as hash.
Thus, when you change them, hash also changes and new cache file is saved.
