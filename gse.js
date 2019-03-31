// var ffi = require('ffi-napi');
var ffi = require('ffi');
const path = require('path');

var Struct = require("ref-struct");

//
var findS = Struct({
    freq: 'long',
    ok: 'bool'
})

const bin = path.join(__dirname, './gse');

var lib = ffi.Library(bin, {
    'GetVersion': ['string', []],
    'LoadDict': ['string', ['string']],
    'AddToken': ['void', ['string', 'long', 'string']],
    'AddTokenForce': ['void', ['string', 'long', 'string']],
    'CalcToken': ['void', []],
    'Find': [findS, ['string']],
    'Cut': ['string', ['string', 'bool']],
    'CutAll': ['string', ['string']],
    'CutSearch': ['string', ['string', 'bool']],
});

function getVersion() {
    lib.GetVersion();
}

function loadDict(path = "zh") {
    return lib.LoadDict(path);
}

function addToken(text, freq, pos = "") {
    lib.AddToken(text, freq, pos);
}

function addTokenForce(text, freq, pos = "") {
    lib.AddTokenForce(text, freq, pos);
}

function calcToken() {
    lib.CalcToken();
}

function find(text) {
    var s = lib.Find(text);
    return {
        freq: s.freq,
        ok: s.ok
    };
}

function cut(str, hmm = false) {
    return lib.Cut(str, hmm).split(" ");
}

function cutAll(str) {
    return lib.CutAll(str).split(" ");
}

function cutSearch(str, hmm = false) {
    return lib.CutSearch(str, hmm).split(" ");
}

exports.getVersion = getVersion;
exports.loadDict = loadDict;
exports.addToken = addToken;
exports.addTokenForce = addTokenForce;
exports.calcToken = calcToken;

exports.find = find;
exports.cut = cut;
exports.cutAll = cutAll;
exports.cutSearch = cutSearch;