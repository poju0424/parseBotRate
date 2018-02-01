#!/usr/bin/python3
fn = "/home/jack/test/a.txt"
try:
    file = open(fn, 'r')
except IOError:
    file = open(fn, 'w')
