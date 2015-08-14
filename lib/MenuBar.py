# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:25:17 2015

@author: chengmf
"""
from Tkinter import *
import sys

class MenuBar(Frame):
    def __init__(self, parent = None, menuBar = None):
        self.menuBar = menuBar
        Frame.__init__(self, parent)
        self.pack(expand = YES, fill = BOTH)
        self.makeMenuBar()
            
    def makeMenuBar(self):
        menubar = Menu(self.master)
        self.master.config(menu = menubar)
        
        for (name, key, items) in self.menuBar:
            pulldown = Menu(menubar)
            self.addMenuItems(pulldown, items)
            menubar.add_cascade(label = name, underline = key, \
                                menu = pulldown)
  
    def addMenuItems(self, menu, items):
        for item in items:
            if item == 'separator': menu.add_separator({})
            elif type(item[2]) != list:
                menu.add_command(label = item[0], underline = item[1], \
                                 command = item[2])
            else:
                pullover = Menu(menu)
                self.addMenuBar(pullover, item[2])
                menu.add_cascade(label = item[0], underline = item[1], \
                                 menu = pullover)
                                 
if __name__ == '__main__':
    
    menuBar = [('file', 0,
                  [('open', 0, lambda: 0), ('quit', 0, sys.exit)]),
               ('edit', 0,
                  [('cut', 0, lambda: 0), ('paste', 0, lambda: 0)])]
                  
    root = Tk()
    MenuBar(root, menuBar).mainloop()
