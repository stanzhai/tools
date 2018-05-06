#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 诡异的编码问题：https://stackoverflow.com/questions/31079412/python-eyed3-unicodeencodeerror-ascii-codec-cant-encode-character-u-xe9-in
# https://stackoverflow.com/questions/42516289/how-to-fix-python-encoding-in-terminal
# https://docs.python.org/3.6/using/cmdline.html#envvar-PYTHONIOENCODING
# locale
# OK: PYTHONIOENCODING=utf-8 python test.py
import sys
import os
import xml.etree.cElementTree as ET
reload(sys)
sys.setdefaultencoding('utf-8')

def multi_get_letter(str_input): 
  if isinstance(str_input, unicode): 
    unicode_str = str_input 
  else: 
    try: 
      unicode_str = str_input.decode('utf8') 
    except: 
      try: 
        unicode_str = str_input.decode('gbk') 
      except: 
        print 'unknown coding' 
        return 
  return_list = [] 
  for one_unicode in unicode_str: 
    return_list.append(single_get_first(one_unicode)) 
  return return_list

def single_get_first(unicode1): 
  str1 = unicode1.encode('gbk') 
  try:     
    ord(str1) 
    return str1 
  except: 
    asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536 
    if asc >= -20319 and asc <= -20284: 
      return 'a' 
    if asc >= -20283 and asc <= -19776: 
      return 'b' 
    if asc >= -19775 and asc <= -19219: 
      return 'c' 
    if asc >= -19218 and asc <= -18711: 
      return 'd' 
    if asc >= -18710 and asc <= -18527: 
      return 'e' 
    if asc >= -18526 and asc <= -18240: 
      return 'f' 
    if asc >= -18239 and asc <= -17923: 
      return 'g' 
    if asc >= -17922 and asc <= -17418: 
      return 'h' 
    if asc >= -17417 and asc <= -16475: 
      return 'j' 
    if asc >= -16474 and asc <= -16213: 
      return 'k' 
    if asc >= -16212 and asc <= -15641: 
      return 'l' 
    if asc >= -15640 and asc <= -15166: 
      return 'm' 
    if asc >= -15165 and asc <= -14923: 
      return 'n' 
    if asc >= -14922 and asc <= -14915: 
      return 'o' 
    if asc >= -14914 and asc <= -14631: 
      return 'p' 
    if asc >= -14630 and asc <= -14150: 
      return 'q' 
    if asc >= -14149 and asc <= -14091: 
      return 'r' 
    if asc >= -14090 and asc <= -13119: 
      return 's' 
    if asc >= -13118 and asc <= -12839: 
      return 't' 
    if asc >= -12838 and asc <= -12557: 
      return 'w' 
    if asc >= -12556 and asc <= -11848: 
      return 'x' 
    if asc >= -11847 and asc <= -11056: 
      return 'y' 
    if asc >= -11055 and asc <= -10247: 
      return 'z' 
    return ''

def main():
  os.chdir(sys.argv[1])
  tree = ET.parse("gamelist.xml")
  root = tree.getroot()
  result = '<?xml version="1.0"?>\n<gameList>\n'
  cmds = ''
  games = {}
  for child in root:
    path = child.find('path')
    name = child.find('name')
    image = child.find('image')
    video = child.find('video')
    if '淘宝奸商' in path.text:
      cur = os.getcwd()
      postfix = path.text.split('.')[-1]
      new_path = './%s.%s' % (name.text, postfix)
      #os.rename(os.path.join(cur, path.text), os.path.join(cur, new_path))
      print 'mv "%s" "%s"' % (os.path.join(cur, path.text), os.path.join(cur, new_path))
      path.text = new_path
      new_image = './flyer/%s.png' % name.text
      #os.rename(os.path.join(cur, image.text), os.path.join(cur, new_image))
      print 'mv "%s" "%s"' % (os.path.join(cur, image.text), os.path.join(cur, new_image))
      image.text = new_image
      new_video = './snap/%s.mp4' % name.text
      #os.rename(os.path.join(cur, video.text), os.path.join(cur, new_video))
      print 'mv "%s" "%s"' % (os.path.join(cur, video.text), os.path.join(cur, new_video))
      video.text = new_video

    n = name.text
    # (ACT) game -> game
    if n[0] == '(':
      n = n[5:]
    # 001 game -> game
    temp = n.split(' ')
    if len(temp) > 1 and temp[0].isdigit():
      n = ' '.join(temp[1:])
    key = single_get_first(n).upper()
    if key == '':
      key = n[0].upper()
    new_name = '%s %s' % (key, n)
    game_info = ''
    game_info += '  <game>\n'
    game_info += '    <name>%s</name>\n' % new_name
    game_info += '    <path>%s</path>\n' % path.text
    if image is not None:
      game_info += '    <image>%s</image>\n' % image.text
    if video is not None:
      game_info += '    <video>%s</video>\n' % video.text
    game_info += '    <desc>%s (Stan 专版)</desc>\n' % n
    game_info += '  </game>\n'
    if key in games:
      games[key].append(game_info)
    else:
      games[key] = [game_info]

  for k in sorted(games.keys()):
    for g in games[k]:
      result += g

  result += '</gameList>\n'
  with open('gamelist.xml', 'w') as f:
    f.write(result)

if __name__ == '__main__':
  main()
