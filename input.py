#!/usr/bin/python3
fn = "/test/a.txt"
try:
    file = open(fn, 'r')
except IOError:
    file = open(fn, 'w')
