# bestlog
![version](https://img.shields.io/badge/version-1.2.1-blue)
![license](https://img.shields.io/badge/license-MIT-brightgreen)
![python_version](https://img.shields.io/badge/python-%3E%3D%203.5-brightgreen)
![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
[![](https://img.shields.io/badge/blog-@encoderlee-red)](https://encoderlee.blog.csdn.net)

this is a simple python logger that logs to file and stdout


I originally wanted to call it 'easylog' but there is already a package with that name on pypi

## Install
```$ pip install bestlog```

## Using
```python
from bestlog import logger
import logging

log = logger.get("test")
# or
log = logging.getLogger("test")

def main():
    log.info("what the fuck")

if __name__ == '__main__':
    logger.init("test")
    main()
```
output:
```
[2022-11-16 21:37:06,032][INFO]: what the fuck
```

you can find log file in the 'logs' folder of the current directory, one log file per day

## Advance

```python
from bestlog import logger
import logging

logger.default_log_path = "/var/log/test/"
logger.default_log_level = logging.DEBUG
logger.default_backup_days = 30

log = logger.get("test")

def main():
    log.debug("what the fuck")

if __name__ == '__main__':
    logger.init("test")
    main()
```
you can specify the path to save the log file

you can set how many days the log file will be retained, default 0 is unlimited

## With tag
```python
from bestlog import logger

class Worker:
    def __init__(self, name):
        self.name = name
        self.log = logger.get("test", name)

    def do_something(self):
        self.log.info("hello")

def main():
    worker1 = Worker("bob")
    worker2 = Worker("jack")
    worker1.do_something()
    worker2.do_something()

if __name__ == '__main__':
    logger.init("test", tag = True)
    main()
```
output:
```
[2022-11-16 21:42:49,469][INFO][bob]: hello
[2022-11-16 21:42:49,470][INFO][jack]: hello
```
you can distinguish between the logs of different workers based on their tag
