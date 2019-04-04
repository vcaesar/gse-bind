# gse-bind

Go efficient text segmentation, binding other language.

[简体中文](https://github.com/vcaesar/gse-bind/blob/master/README_zh.md)

## Install gse
```
npm install gse
```

## example

```js
var gse = require('gse');

gse.loadDict();
console.log(gse.cut("我在大雨刚停的夜晚", true));
```

## Build from source code:

### Install gse
```
go get -u github.com/go-ego/gse
```

### [Build-tools](http://github.com/vcaesar/gocs)
```
go get -v github.com/vcaesar/gocs
```

### Building

```
gocs -n gse
```

### Install npm modules 

```
npm install
```