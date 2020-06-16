

with open(f'C:\\Users\\Александр\\Desktop\\itoolabs.txt') as f:
    fr = f.read().replace('\t', ' ').splitlines()
    print(fr)
    print(type(fr))
