## Syntax:
# import math                       # whole module
# from pathlib import Path          # specific name/module
# import numpy as np                # alias creation
# from mypackage import mymodule    # package -> module

# __all__ = ["public_function"] #inside a module: control as public API
# __name__ == "__main__" #module guard: Only runs when the file is executed directly

from gpay_utils import format_inr, parse_inr

if __name__ == "__main__":
    price = 49999
    display = format_inr(price) 
    print(display)
    print(parse_inr(display))

