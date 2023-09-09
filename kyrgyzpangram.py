def ispangram(s: str) -> bool:
    s = s.lower()
    alphs = 'йцуүкенңгшщзхъфывапроөлджэячсмитьбю'
    for i in alphs:
        if i not in s:
            return f"{False} -> ({i})"
    return True

vd = ispangram('')
print(vd)