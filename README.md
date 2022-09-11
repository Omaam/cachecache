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

This will make the .cache folder and create a binary object in this.
The wrapper uses source code, arguments, and keyword arguments as a hash.
Thus, when you change them, the hash also changes, and a new cache file
is saved.
