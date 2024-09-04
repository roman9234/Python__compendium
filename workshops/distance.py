from functools import total_ordering
from typing import Any


class Centemeter:
    pass
q = Centemeter()

class Meter:
    pass

print(type(q) in [Meter, Centemeter])