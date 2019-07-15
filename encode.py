import base91
import qrcode
import random
import string

original_string = "===This is some test message===="


max_string_length = 507
def get_padding( length ):
	return "".join( random.SystemRandom().choice( string.ascii_letters + string.digits ) for _ in range( length ) )
def make_max_image_possible( message ):
	original_length = len( message )
	if original_length > max_string_length:
		print( "Message Already At Max Size , Can't Add any Padding" )
		return message[ 0:max_string_length ]
	remaining_space = ( max_string_length - len( message ) )
	print( "Adding " + str( remaining_space ) + " characters of padding")
	return message + get_padding( remaining_space )

encode_string = make_max_image_possible( original_string )
print( encode_string )
encode_string = base91.encode( encode_string )
print( encode_string )
img = qrcode.make( encode_string )
img.save( "test444.png" , "PNG" )