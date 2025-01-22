#!/usr/bin/env python3

# Author: Sangeeth Vethanayagam
# Author ID: 189353238
# Date Created: 01/25/2025

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

count = timer
while count > 0:
    print(count)
    count = count - 1
print('blast off!')
