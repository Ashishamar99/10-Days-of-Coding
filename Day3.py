inp = input('Enter the number and then the string seperated by a comma: ')
inp = inp.split(',')
n = int(inp[0])
s = inp[1]
if n == len(s):
    s = list(s)
    s.sort()
    print(''.join(s))
else:
    print('Enter the length equal to n.')