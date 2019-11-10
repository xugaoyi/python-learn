# Q4
def dayUP(df): # def定义函数dayUP，形参df
  dayup = 1
  for i in range(365):
    if i % 7 in [6, 0]:
      dayup = dayup * (1 - 0.01) # 休息日固定下降
    else:
      dayup = dayup * (1 + df) # 工作日进步
  return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78: # while循环
  dayfactor += 0.001
print('工作日努力进步{:.1f}%才能追平A君'.format(dayfactor*100))