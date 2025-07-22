d={
    "a":1,
    'b':2,
    'l':[3,4,5],
    "u":"orange",
    "i":"blue",
    "v":"pink"
}

d.update({'a':10,'t':25})
print(d)
print(d.get('z'))
print(d['a']) #else error