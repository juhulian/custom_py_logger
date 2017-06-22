# custom_py_logger
yet a other wrapper for python2-print ;-)

## log-levelz
0. error, warning, info(2), debug(2)  (default)
1. error, warning, info(2)
2. error, warning
3. error
4. (nothing)

```python
    from custom_py_logger import logger

    class MyClass:
         def __init__(self):
             self.log = logger.Log(self.__class__.__name__, level=1)
             self.log.debug("hello")  #
             self.log.info2("hello")  # 18:41:04 MyClass [ii] hello
```
