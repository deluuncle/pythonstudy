import re
content = "(百度)www.baidu.com"
result = re.match("\(百度\)www\.baidu\.com",content)
# result2 = re.match("^Hello.*Demo$",content)


# result3 = re.match("^He.*(\d+).*Demo$",content)
# final_re = result.group()
# f_re = result.span()
print(result)
