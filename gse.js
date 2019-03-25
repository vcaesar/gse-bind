// var ffi = require('ffi-napi');
var ffi = require('ffi');
var Struct = require("ref-struct");


var findS = Struct({
    freq: 'long',
    ok: 'bool'
})

var lib = ffi.Library("gse", {
    'GetVersion': ['string', []],
    'LoadDict': ['string', ['string']],
    'AddToken': ['void', ['string', 'long', 'string']],
    'AddTokenForce': ['void', ['string', 'long', 'string']],
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