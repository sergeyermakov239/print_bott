import win32print
import win32api

printers=win32print.EnumPrinters(2)
print(printers)
name='print10 PCL6'
print(name)

printdefaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
  ## начинаем работу с принтером ("открываем" его)
handle = win32print.OpenPrinter(name, printdefaults)

win32print.StartDocPrinter(handle, 1, ['instruction.pdf', None, "raw"])

win32api.ShellExecute(0,"print",'instruction.pdf','/d:"%s"' %name,".",0)
