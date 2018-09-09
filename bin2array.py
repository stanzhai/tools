# 将指定的文件转换为js的数组
# 用于：https://ns.stanzhai.site/
import binascii

if __name__ == "__main__":
  with open('/Users/stan/Downloads/hekate_ctcaer_4.0.bin', 'rb') as f:
    all = f.read()
    with open('/Users/stan/Downloads/hekate_ctcaer_4.0.js', 'w') as w:
      w.write("const hekate_ctcaer = new Uint8Array([")
      for d in all:
        w.write("0x%s," % binascii.b2a_hex(d))
      w.seek(-1, 2)
      w.write("]);")
