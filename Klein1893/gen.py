def color(r,g,b):
  return "r='%d' g='%d' b='%d'" % (r,g,b)

balls = [("a", color(255,0,0)), ("b", color(0,255,0)), ("c", color(0,0,255))]
for t in range(2):
  newballs = []
  for b, bcolor in balls:
    for mirror, _ in balls:
      # Don't reflect B in M if B is an image inside M already.
      if b.startswith(mirror): continue
      newball = mirror+"C"+b+"D"
      print("<command name='Mirror'><input a0='%s' a1='%s'/><output a0='%s'/></command>" % (b, mirror, newball))
      print("<element type='conic' label='%s'><show object='true' label='false' ev='4'/>" % newball)
      print("  <objColor %s alpha='0.1'/>" % bcolor)
      print("  <lineStyle thickness='4' type='0' typeHidden='1'/>")
      print("</element>")
      newballs += [(newball, bcolor)]
  balls += newballs
