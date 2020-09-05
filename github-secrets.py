#!/usr/local/bin/python3

import sys, argparse, json

from base64 import b64encode
from nacl import encoding, public

def encrypt( encrypt_key: str, secret_value: str ) -> str:
    #private_key = public.PrivateKey.generate()
    public_key = public.PublicKey( encrypt_key.encode( "utf-8" ), encoding.Base64Encoder() )
    sealed_box = public.SealedBox( public_key )
    encrypted = sealed_box.encrypt( secret_value.encode( "utf-8" ) )
    ### print(encrypted)
    return b64encode( encrypted ).decode( "utf-8" )

def main():
    ## print ( 'Total Arguments?:', format( len( sys.argv ) ) )
    ## print ( '   Argument List:', str( sys.argv ) )
    parser = argparse.ArgumentParser()
    parser.add_argument( '--public-key', dest='public_key',  type=str, help='Encryption Public-Key' )
    parser.add_argument( '--content', dest='content',  type=str, help='Source Content' )
    options = parser.parse_args()
    ## print( json.dumps( { "encrypted_value" : encrypt( options.public_key, options.content ), "key_id" : encrypt_key } ) )
    print( encrypt( options.public_key, options.content ) )

if __name__ == '__main__':
    main()
