# import math_utils
# from math_utils import add, sub
# from math_utils import *

# # print(math_utils.add(20, 30))
# print(add(1, 9))


# from my_Package_37 import math_utils, string_util

# math_utils.add(2, 3)
# string_util.to_upper("Rohit")


from pathlib import Path
import sys

# Ensure project root is on sys.path so sibling packages can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from my_Package_37.math_utils import add
from my_Package_37.string_util import to_upper

print(add(3, 4))
print(to_upper("rohit"))
