import re

line = "aaaabooobabbby123"
regex_str = ".*(babbb|babbby)"

match = re.findall(regex_str,line)
print(match)
# match_obj = re.match(regex_str,line)
# if match_obj:
#     print(match_obj.group(3))