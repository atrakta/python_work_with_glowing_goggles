# how decrypt python dzen from this.s
import this

pd=''

for ch in this.s:
  if ch not in this.d.keys():
    pd=pd+ch
  else:
    pd=pd+this.d[ch]

print(pd)
