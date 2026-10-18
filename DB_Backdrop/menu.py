import os
import sys
import nuke
import nukescripts

sys.dont_write_bytecode = True

#setup top menu
toolbar = nuke.menu("Nuke")
db_tools_menu = toolbar.addMenu("DB Tools")
db_backdrop_menu = db_tools_menu.addMenu("DB Backdrop")

#add menu items
import db_backdrop
db_backdrop_menu.addCommand('Create new', 'db_backdrop.db_backdrop_add()', "alt+b", shortcutContext=2)
db_backdrop_menu.addCommand('Align to grid', 'db_backdrop.db_backdrop_align()', "shift+alt+b", shortcutContext=2)