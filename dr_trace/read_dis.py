dis = {}
with open('dis.txt', 'rb') as fh:
    data = fh.read()
    spl = data.split()
    print spl[1]
