from PyQt5 import uic

with open("#.py fil you want to convert#","w",encoding="utf-8") as fout:
    uic.compileUi("#.ui file name you can determine#",fout)
