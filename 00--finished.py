# menuTitle : 00: Finished - No Mark
# shortCut  : command+control+shift+0
"""
  Mark currently-selected glyphs as "Finished,"
  so it's clear that they need no known work.
"""

from markLib.markGlyphs import markGlyphs
from markLib.settings import markSettings

color = None

f = CurrentFont()
markGlyphs(f, markSettings["finished"])
