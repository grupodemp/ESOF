import sys
import HYP_Utils
from PIL import Image

scriptDir = HYP_Utils.GetDemoDir()

PIL_Version = Image.VERSION

img_filename = "%s/teste.jpg" % scriptDir
im = Image.open(img_filename)
im.save("%s/teste.png" % scriptDir)

