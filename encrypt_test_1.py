import base64

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import serialization

def temp_save_encrypted_message( encrypted_base_64_string ):
	with open( "temp_encrypted_base_54_string.txt" , "w" ) as f:
		f.write( encrypted_base_64_string )

def save_key_pair( private_key , public_key ):

	private_pem = private_key.private_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PrivateFormat.PKCS8,
		#encryption_algorithm=serialization.BestAvailableEncryption(b'testing124')
		encryption_algorithm=serialization.NoEncryption()
	)

	public_pem = public_key.public_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PublicFormat.SubjectPublicKeyInfo
	)

	private_key_lines = private_pem.splitlines()
	with open( "new_private_key" , "w" ) as f:
		f.writelines( map( lambda s: s + "\n" , private_key_lines ) )
		# for line in private_key_lines:
		# 	print( line )
		# 	f.write( line )

	public_key_lines = public_pem.splitlines()
	with open( "new_public_key.pub" , "w" ) as f:
		f.writelines( map( lambda s: s + "\n" , public_key_lines ) )
		# for line in public_key_lines:
		# 	print( line )
		# 	f.write( line )

def generate_key_pair():
	# GENERATE NEW KEYPAIR
	keysize = ( 2**13 ) # 8192
	print( keysize )
	private_key = rsa.generate_private_key(
		public_exponent=65537,
		key_size=keysize,
		backend=default_backend()
	)
	public_key = private_key.public_key()
	return [ private_key , public_key ]

def encrypt( plain_text , public_key ):
	# ENCRYPTION
	cipher_text_bytes = public_key.encrypt(
		plaintext=plain_text.encode( "utf-8" ),
		padding=padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA512(),
			label=None
		)
	)

	# CONVERSION of raw bytes to BASE64 representation
	#cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)
	cipher_text = base64.b64encode(cipher_text_bytes)
	return cipher_text

def decrypt( enrypted_text , private_key ):
	# DECRYPTION
	decrypted_cipher_text_bytes = private_key.decrypt(
		ciphertext=base64.urlsafe_b64decode(cipher_text),
		padding=padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA512(),
			label=None
		)
	)
	decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')
	return decrypted_cipher_text



new_keypair = generate_key_pair()
save_key_pair( new_keypair[ 0 ] , new_keypair[ 1 ] )
encrypted_message_text = encrypt( "this is a test message" , new_keypair[ 1 ] )
print( encrypted_message_text )
temp_save_encrypted_message( encrypted_message_text )
#print( new_keypair )
