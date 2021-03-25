e2f = dict(dog='chien', cat='chat', walrus='morse')
#print(e2f)
#print(e2f['walrus'])
"""e2f_list = list(e2f.items())
print(e2f_list)
f2e = []
tmp = []
for i in (0, 2, 1):
    tmp += list(e2f_list[i])
    print(tmp)"""
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)
print(set(e2f.keys()))