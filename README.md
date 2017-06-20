# custom_py_logger
yet a other wrapper for python-print ;-)

```python
    from custom_py_logger import logger

    class MyClass:
         def __init__(self):
             self.log = logger.Log(self.__class__.__name__)
             self.log.info("hello")
```
