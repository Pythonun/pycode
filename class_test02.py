class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    local_logo = 'CocaCola'
coke_for_me = CocaCola()
coke_for_you = CocaCola()
coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐'#创建实例属性
coke_for_USA = CocaCola()
print(coke_for_USA.local_logo)
print(coke_for_China.local_logo)#打印实例属性
print(CocaCola.formula)
print(coke_for_me.formula)
for element in coke_for_me.formula:
    print(element)
