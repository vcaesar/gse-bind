# gse-bind

Go 高性能分词, binding 其他编程语言.

## 安装 gse
```
npm install gse
```
or 

```
sudo cnpm install gse
```
```
npm --registry=http://r.cnpmjs.org install gse
```

## example

```js
var gse = require('gse');

gse.loadDict();
console.log(gse.cut("我在大雨刚停的夜晚", true));
```

## 从源码部署:

### Install gse
```
go get -u github.com/go-ego/gse
```
```
git clone https://github.com/vcaesar/gse-bind
```

### [Build-tools](https://github.com/vcaesar/gocs)
```
go get -v github.com/vcaesar/gocs
```

### Building

```
cd gse-bind
```

```
gocs -n gse
```

### 安装 npm modules 

```
npm install
```

### python

```
pip install cffi
```

```python
import sys

sys.path.append("..")
import gse

# load
gse.loadDict()
print(gse.cut('我在大雨刚停的夜晚', True))
```