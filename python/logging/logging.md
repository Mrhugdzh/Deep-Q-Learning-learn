## 日志模块组件

日志模块具有四个主要组件：

- 记录器：公开了应用代码直接使用的接口
- 处理程序：将日志（记录器创建）发送到适当的目的地
- 过滤器：提供了更细粒度的功能，用于确定要输出的日志
- 格式化程序：最终输出中指定日志的布局

## Python日志层次结构

Python记录器形成了一个层次结构。名为main的记录器是*main.new*的父级

**子记录器将消息传播到与其先祖记录器关联的处理程序**，因此，不必为应用中的所有记录器东一和配置处理程序。为顶级记录器配置处理程序并根据需要创建子记录器就足够了。

## 日志的级别

级别用于表示时间的严重性。有六个日志级别：

- 危机：CRITICAL
- 错误：ERROR
- 警告：WARRING
- 信息：INFO
- 调试：DEBUG
- 没有设置

如果日志级别设置为WARING，那么所有的WARRING， ERROR和CRITICAL消息都会写入日志文件或控制台。如果日志级别设置为ERROR，则仅记录ERROR和CRITICAL消息。

记录器的概念是有级别的，如果未在记录器上显示设置级别，则将其父级的级别用作其有效级别，依次搜索，知道找到有显示设置的级别。

## 根记录器

所有记录器都是根记录器的后代。每个记录器将日志消息传递至其父级。使用 ``getLogger(name)``方法创建新的记录器，调用不带名称的函数 ``getLogger()``返回root记录器

***根记录器式中具有显示级别集，默认情况下为WARRING。***

根发信人位于层次结构的顶部，即时未配置，也始终存在。通常，程序或库不应该直接登记到根记录器。而是应该配置改程序的特定记录器。跟记录器可以用于轻松打开和关闭所有库中的所有记录器。

## Python 有效日志级别

有效日志级别是显示设置的级别或由记录器的父级确定的级别

## Python日志处理程序

处理程序是一个对象，负责将适当的日志信息（基于日志信息的严重性）调度到处理程序的制定目标。

处理程序向级别一样传播。如果记录器未设置处理程序，择期祖先链将搜索处理程序

## 日志格式化程序

格式化程序是一个对象，用于配置日志的最终顺序，结构和内容。除消息字符串外，日志还包括日期和时间，日志名称和日志级别严重性。

```python
logger=logging.getLogger('dev')
logger.setLevel(logging.INFO)

consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(consoleHandler)
# 设置一个Formatter
formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s')
consoleHandler.setFormatter(formatter)

logger.info('This is a info message')
```


## Python 日志basicConfig

basicConfig()配置根记录器，它通过使用默认格式化程序创建流处理程序来为日志系统进行基本配置。如果没有卫根记录器定义处理程序，则debug()、info()、warning()、error()和critical()自动调用basicConfig()

```python
logging.basicConfig(filename='test.log', format='%(asctime)s %(filename)s : %(message)s', level=logging.INFO)

logging.info('this is a info message')
logging.debug('this is a debug message')
logging.debug('this is a debug msg')
logging.warning('this is a warning message')
logging.error('this ia a error')
```

## Python日志配置文件

log.conf

```
[loggers]
keys=root, dev

[handlers]
keys=consoelHandler

[formatters]
keys=extend, simple

[logger_root]
level=INFO
handlers=consoelHandler

[logger_dev]
level=INFO
handlers=consoelHandler
qualname=dev
propagate=0

[handler_consoelHandler]
class=StreamHandler
level=INFO
formatter=extend
args=(sys.stdout,)

[formatter_extend]
format=%(asctime)s - %(name)s - %(levelname)s :  - %(message)s

[formatter_simple]
format=%(filename) - %(message)
```

读取配置文件，使用logging.config.fileConfig()

```python
import logging
import logging.config

logging.config.fileConfig(fname='log.conf')

logger=logging.getLogger('dev')
logger.info('This is a info message')
```

## Python 日志变量

## Python日志格式化日期信息

日期信息包含在asctime日志的日志信息中。使用datefmt配置选项，我们可以格式化日期时间字符串。

```python
import logging
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

log_format='%(asctime)s %(filename)s : %(message)s'
datefmts='%Y-%m-%d %H:%M:%S'

logging.basicConfig(filename='./test.log', format=log_format, datefmt=datefmts)

logging.error('sssss')
```
