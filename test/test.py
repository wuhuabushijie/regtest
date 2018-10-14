import re

# line = "aaaabooobabbby123"
# regex_str = ".*(babbb|babbby)"
#
# match = re.findall(regex_str,line)
# print(match)
# match_obj = re.match(regex_str,line)
# if match_obj:
#     print(match_obj.group(3))

line = """
    出生日期：
    2016年10月6日
    2016-10-6
    2016/10/6
    2016/10/06
    2016年10月
    2016/06
    2016/6
    2016-06
"""
regex_str = "\s*\S*?(\d{4}[年/-]\d{1,2}[月/-]{0,1}\d{0,2}日{0,})"

match = re.findall(regex_str,line)
for dates in match:
    print(dates)