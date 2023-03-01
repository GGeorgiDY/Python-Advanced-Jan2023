from math import log, e

number = int(input())
logarithm_base = input()

base = e if logarithm_base == 'natural' else int(logarithm_base)
print(f"{log(number, base):.2f}")

# идеята тук е ако имеме natural,базата ни ще е непоровото число. Ако обаче не е natural ще е някакъв инт

# 10
# natural

# 10
# 10

