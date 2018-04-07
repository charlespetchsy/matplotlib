import pytest
import matplotlib.colors as mcolors

new_palette = {'color1': '#952e8f', 'color2': '#894585', 'color3': '#70b23f'}

def test_add_palette():
  mcolors.registerPalette('newPalette', new_palette)
  all_palettes = mcolors.getPalettes()
  assert (('newPalette' in all_palettes) and (all_palettes['newPalette'] == new_palette))

def test_update_palette():
  updated_palette = {'color1': '#69d84f', 'color2': '#a8ff04', 'color3': '#70b23f', 'color4':'#a5a391'}
  mcolors.updatePalette('newPalette', updated_palette)
  all_palettes = mcolors.getPalettes()
  assert (('newPalette' in all_palettes) and (all_palettes['newPalette'] == updated_palette))
