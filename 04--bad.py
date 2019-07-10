# menuTitle : 04: Bad
# shortCut  : command+control+shift+4
"""
  Mark currently-selected glyphs as "Bad,"
  so it's clear they should be fixed later.
"""

from markLib.markGlyphs import markGlyphs, markSettings

f = CurrentFont()
markGlyphs(f, markSettings["bad"])