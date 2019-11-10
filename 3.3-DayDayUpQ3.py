# 工作日的力量Q3
dayup = 1.0 # 基数
dayfactor = 0.01 # 每天向上参数
for i in range(365): # 循环365天
  if i % 7 in [6, 0]: # 周末
    dayup = dayup * (1 - dayfactor) # 下降
  else:
    dayup = dayup * (1 + dayfactor) # 提高
print('工作日的力量：{:.2f}'.format(dayup))
