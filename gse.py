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
		GoInt freq;
		bool ok;
	} Find_r;

	char* GetVersion();
	char* LoadDict(char* p0);
	void AddToken(char* p0, GoInt p1, char* p2);
	void AddTokenForce(char* p0, GoInt p1, char* p2);
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
    lib.AddToken(ch(text), freq, ch(pos))


def addTokenForce(text, freq, pos=""):
    lib.AddTokenForce(ch(text), freq, ch(pos))


def calcToken():
    lib.CalcToken()

#


def find(text):
    s = lib.Find(ch(text))
    return s.freq, s.ok


def arr(s):
    st = bytes.decode(f_str(s))
    return st.split(' ')


def cut(sentence, hmm=False):
    s = lib.Cut(ch(sentence), hmm)
    return arr(s)


def cutAll(sentence):
    s = lib.CutAll(ch(sentence))
    return arr(s)


def cutSearch(sentence, hmm=False):
    s = lib.Cut(ch(sentence), hmm)
    return arr(s)
