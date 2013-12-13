import os
import sys


def re_throw_ex(ex_type, message, inner_ex):
  raise ex_type, "{0}{sep}Inner Exception: {1}".format(message, inner_ex, sep=os.linesep), sys.exc_info()[2]
