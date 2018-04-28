d = dict()

d['black']=[0,1]
d['brown']=[1,10]
d['red']=[2,100]
d['orange']=[3,1000]
d['yellow']=[4,10000]
d['green']=[5,100000]
d['blue']=[6,1000000]
d['violet']=[7,10000000]
d['grey']=[8,100000000]
d['white']=[9,1000000000]

a = input()
b = input()
c = input()

print((d[a][0]+d[b][0])*d[c][1])
