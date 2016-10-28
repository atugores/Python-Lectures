#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from time import sleep


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('USAGE: A parameter should be provided.')
        sys.exit()

    print('your input was ' + sys.argv[1])
    sleep(1)
    print('finished')

