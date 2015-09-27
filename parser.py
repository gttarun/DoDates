# Parsing Cases: 

# September 31, 2015 
# September 31 2015
# September 31
# Sep 31 2015
# Sep 31
# 31 September

# 8/31/2015
# 8/31/15
# 8/31

import time, re

subject = "Aug06 Aug2006, August 2 2008, 19th August 2006, 08-06, 01-08-06"

for match in re.finditer(
    r"""(?ix)             # case-insensitive, verbose regex
    \b                    # match a word boundary
    (?:                   # match the following three times:
     (?:                  # either
      \d+                 # a number,
      (?:\.|st|nd|rd|th)* # followed by a dot, st, nd, rd, or th (optional)
      |                   # or a month name
      (?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)
      |					  # or full month name
      (?:(?:January|Febuary|March|April|May|June|July|August|September|October|November|December)[a-z]*)
     )
     [\s./-]*             # followed by a date separator or whitespace (optional)
    ){3}                  # do this three times
    \b""",                # and end at a word boundary. 
    subject):
	match.start()
	match.end()
	print match.group()

