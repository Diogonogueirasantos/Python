from random import choice

def recursividade(caso):
  caso_base = 100
  if caso < caso_base:
    caso += 1
    print(caso)
    return recursividade


recursividade(11)