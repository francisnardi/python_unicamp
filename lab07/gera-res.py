# -*- coding: utf-8 -*-
#
# Script para testes do programa main.py utilizando
#  arquivos de entrada: arq<i>.in
#  arquivos de saída:   arq<i>.res
# Serão criados arquivos arq<i>.res para comparação com arq<i>.res

import os
import shutil
import sys
import re

pattern = re.compile("arq[0-9]+.in\Z")

for filename in os.listdir(".") :
  if pattern.match(filename) :
    resfile = re.sub(r"in","res",filename)
    print (resfile)
    os.system("python3 ../sols/lab07.py < " + filename +
               " > " + resfile)
