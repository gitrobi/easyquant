
from custom import fixedmainengine

m = fixedmainengine.FixedMainEngine("xq", ext_stocks=['159915, 162411'])
m.load_strategy()
m.start()
