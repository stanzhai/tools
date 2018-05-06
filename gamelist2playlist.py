#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Usage: python ~/gamelist2playlist.py ~/roms/cps1/gamelist.xml /tmp/cores/fbalpha_libretro.so "Arcade (FB Alpha)" cps1 
import sys
import os
import xml.etree.cElementTree as ET
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
  game_list = sys.argv[1]
  core = sys.argv[2]
  core_name = sys.argv[3]
  play_list = sys.argv[4]
  base_path = '/'.join(game_list.split('/')[0:-1])
  tree = ET.parse(game_list)
  root = tree.getroot()
  result = ''
  for child in root:
    path = child.find('path')
    rom_path = '%s/%s' % (base_path, path.text[2:])
    name = child.find('name')
    result += '%s\n' % rom_path
    result += '%s\n' % name.text
    result += '%s\n' % core
    result += '%s\n' % core_name
    result += 'DETECT\n'
    result += '%s.lpl\n' % play_list

  with open('%s.lpl' % play_list, 'w') as f:
    f.write(result)

if __name__ == '__main__':
  main()
