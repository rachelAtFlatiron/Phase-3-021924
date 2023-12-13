#!/usr/bin/env python3

#✅ 5. Import the pet and cat class to use in debug.py

import ipdb
from lib.cat import Cat 

rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)

ipdb.set_trace()