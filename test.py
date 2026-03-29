import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ibt_code.detector import ibtcode_detect

text = "This is the third time I'm asking respond."

result = ibtcode_detect(text)
print(result)