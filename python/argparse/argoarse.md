
## argparse

解析**sys.argv**中定义的参数

argparse模块还有自动生成帮助和使用信息，并在用户为程序提供无效参数时发出错误

是标准模块，不需要安装

使用 ``ArgumentParser``创建一个解析器，并使用 ``add_argument()``添加一个新参数，参数是可选的，必须的或定位的


## argparse可选参数

```python
import argparse

parse=argparse.ArgumentParser()

parse.add_argument('-o', '--output', action='store_true', help='show output')

args=parse.parse_args()

if args.output:
    print('this is some output')

```
