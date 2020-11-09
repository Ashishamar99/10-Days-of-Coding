n = int(input())
min = ''
max = ''

for i in range(n):
    inp_str = input()
    if (inp_str < min) or (min == ''): min = inp_str
    if (inp_str > max) or (max == ''): max = inp_str

print(min, max)