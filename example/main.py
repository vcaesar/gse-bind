import sys

sys.path.append("..")
import gse

# load
gse.loadDict()
print(gse.cut('我在大雨刚停的夜晚', True))
print(gse.find("大雨"))