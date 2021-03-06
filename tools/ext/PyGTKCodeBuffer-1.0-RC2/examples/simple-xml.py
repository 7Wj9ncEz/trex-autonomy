#!/usr/bin/python
import gtk
from gtkcodebuffer import CodeBuffer, SyntaxLoader, add_syntax_path

#
# This example shows how to use the CodeBuffer. 
#   Note: You need to have PyGTKCodeBuffer installed!

txt = """<?xml version="1.0"?>
<!-- a <comment> -->
<DocumentRoot attribute="value">
    Some &gt;text&lt;...
    <ns:tag>content</ns:tag>
</DocumentRoot> """

lang = SyntaxLoader("xml")
buff = CodeBuffer(lang=lang)

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
scr = gtk.ScrolledWindow()
win.add(scr)
scr.add(gtk.TextView(buff))
        
win.set_default_size(300,200)
win.show_all()
win.connect("destroy", lambda w: gtk.main_quit())
        
buff.set_text(txt)
        
gtk.main()        
