import os
import sys


def re_throw_ex(ex_type, message, inner_ex):
  raise (
    ex_type,
    "{0}{sep}Inner Exception: {1}{sep}\t{2}".format(message, type(inner_ex), inner_ex, sep=os.linesep),
    sys.exc_info()[2] #this is the traceback
  )
