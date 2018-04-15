import math

def principal():
  print "How to use: Enter chainstay and error margin (should be around 0.3)"
  print "Press 'ctrl+C' to close"

  magic_calculator()

def magic_calculator():

  # print "Init calculator"

  get_values()

  posibles = []

  for i in range(30, 55):
    for j in range(11, 25):
      ring_rad = i*chain_unit/(2*math.pi)
      cog_rad = j*chain_unit/(2*math.pi)
      # print "chainstay cuadrado: {}".format(math.pow(chainstay, 2))
      # print "resta de radios cuadrado: {}".format(math.pow(ring_rad-cog_rad, 2))
      c_sqr = math.pow(chainstay, 2) - math.pow(ring_rad-cog_rad, 2)
      c = math.sqrt(c_sqr)
      # print "c: {}".format(c)
      alpha = math.asin(c/chainstay)
      # print "alpha: {}".format(alpha)
      cr_percent = i*chain_unit*(2*math.pi - 2*alpha)/(2*math.pi)
      cog_percent = j*chain_unit*(2*alpha)/(2*math.pi)
      total = 2*c + cr_percent + cog_percent
      links = total / chain_unit
      if links%2 < 1:
        measure = links-math.floor(links)
        if measure < margen:
          # print "For ({},{}): c={} links={}, measure={}, total={}".format(i,j,c, links, measure, total)
          # print "Total links = {}".format(links)
          posibles.append((i,j,links))

  print "Printing all posibles (chainring, cog, #links) for {} mm chainstay".format(chainstay)
  for value in posibles:
      print value
  print "Calculator finished"

def get_values ():
  #Return true if chainring is given
  # print "Getting values"

  global chainstay
  global margen
  chainstay = int(raw_input("Enter chainstay: "))
  margen = float(raw_input("Enter margin: "))
  # print "ok then its {} and {} mgn".format(chainstay, margen)

#Global scope
print "Hello, this is magic ratio app"
chainstay = 0
margen = 0.0
chain_unit = 12.7 #milimeters
while 1:
    principal()
