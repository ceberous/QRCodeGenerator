import base91

from pyzbar.pyzbar import decode
from PIL import Image
x_1_image = Image.open( "test444.png" )

result = decode( x_1_image )

text = result[ 0 ].data
print( text )

decoded = base91.decode( text )
print( decoded )