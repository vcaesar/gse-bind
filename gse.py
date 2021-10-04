# // Copyright 2016 The go-vgo Project Developers. See the COPYRIGHT
# // file at the top-level directory of this distribution and at
# // https://github.com/go-vgo/robotgo/blob/master/LICENSE
# //
# // Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# // http://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# // <LICENSE-MIT or http://opensource.org/licenses/MIT>, at your
# // option. This file may not be copied, modified, or distributed
# // except according to those terms.

from __future__ import print_function
import sys
import os
from cffi import FFI

is_64b = sys.maxsize > 2**32

ffi = FFI()
if is_64b:
    ffi.cdef("typedef long GoInt;\n")
else:
    ffi.cdef("typedef int GoInt;\n")

ffi.cdef("""
	typedef struct {
		double freq;
        char* pos;
		bool ok;
	} Find_r;

	char* GetVersion();
	char* LoadDict(char* p0);
	char* AddToken(char* p0, double p1, char* p2);
	char* AddTokenForce(char* p0, double p1, char* p2);
	void CalcToken();

	//
	Find_r Find(char* p0);
	char* Cut(char* p0, bool p1);
	char* CutAll(char* p0);
	char* CutSearch(char* p0, bool p1);
""")

dir = os.path.dirname(__file__)
bin = os.path.join(dir, "./gse")

lib = ffi.dlopen(bin)


def ch(s):
    return s.encode('utf-8')


def f_str(cs):
    return ffi.string(cs)


def getVersion():
    return f_str(lib.GetVersion())


def loadDict(path="zh"):
    return f_str(lib.LoadDict(ch(path)))


def addToken(text, freq, pos=""):
    return lib.AddToken(ch(text), freq, ch(pos))


def addTokenForce(text, freq, pos=""):
    return lib.AddTokenForce(ch(text), freq, ch(pos))


def calcToken():
    lib.CalcToken()


###


def find(text):
    s = lib.Find(ch(text))
    return s.freq, bytes.decode(f_str(s.pos)), s.ok


def arr(s):
    st = bytes.decode(f_str(s))
    return st.split(' ')


def cut(text, hmm=False):
    s = lib.Cut(ch(text), hmm)
    return arr(s)


def cutAll(text):
    s = lib.CutAll(ch(text))
    return arr(s)


def cutSearch(text, hmm=False):
    s = lib.Cut(ch(text), hmm)
    return arr(s)
