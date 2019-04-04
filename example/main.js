// var gse = require('gse');
var gse = require('../gse');

gse.loadDict();
gse.addToken("大雨刚停", 10);
gse.addTokenForce("今天上午", 10, "n");
console.log(gse.find("今天上午"));

console.log(gse.cut("我在大雨刚停的夜晚", true));
console.log(gse.cutAll("我在大雨刚停的夜晚"));
console.log(gse.cutSearch("我在大雨刚停的夜晚", true));