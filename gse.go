// Copyright 2016 The go-vgo Project Developers. See the COPYRIGHT
// file at the top-level directory of this distribution and at
// https://github.com/go-vgo/robotgo/blob/master/LICENSE
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// http://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or http://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

package main

import "C"

import (
	"fmt"
	"strings"

	"github.com/go-ego/gse"
)

func ch(str string) *C.char {
	return C.CString(str)
}

func str(ch *C.char) string {
	return C.GoString(ch)
}

func sf(err error) string {
	return fmt.Sprintf("%s", err)
}

func toStr(arr interface{}) string {
	return strings.Trim(fmt.Sprint(arr), "[]")
}

//export GetVersion
func GetVersion() *C.char {
	s := gse.GetVersion()
	return ch(s)
}

var seg gse.Segmenter

//export LoadDict
func LoadDict(path *C.char) *C.char {
	err := seg.LoadDict(str(path))

	return ch(sf(err))
}

//export AddToken
func AddToken(text *C.char, freq float64, pos *C.char) *C.char {
	err := seg.AddToken(str(text), freq, str(pos))
	return ch(sf(err))
}

//export AddTokenForce
func AddTokenForce(text *C.char, freq float64, pos *C.char) *C.char {
	err := seg.AddTokenForce(str(text), freq, str(pos))
	return ch(sf(err))
}

//export CalcToken
func CalcToken() {
	seg.CalcToken()
}

//export Find
func Find(text *C.char) (float64, string, bool) {
	return seg.Find(str(text))
}

//export Cut
func Cut(text *C.char, hmm bool) *C.char {
	arr := seg.Cut(str(text), hmm)

	return ch(toStr(arr))
}

//export CutAll
func CutAll(text *C.char) *C.char {
	arr := seg.CutAll(str(text))

	return ch(toStr(arr))
}

//export CutSearch
func CutSearch(text *C.char, hmm bool) *C.char {
	arr := seg.CutSearch(str(text), hmm)

	return ch(toStr(arr))
}

func main() {} // Required but ignored
