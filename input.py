#!/usr/bin/python3
fn = "a.txt"
try:
    file = open(fn, 'r')
except IOError:
    file = open(fn, 'w')
