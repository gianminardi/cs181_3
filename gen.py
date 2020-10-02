import sys
import socket
import cryptography
from os import _exit as quit
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend





def generate_keys(name):
    '''Generates RSA public and private keys and stores them in seperate txt files with name variable
    Name--> String
    Returns: List with privatekey, pubkey generated (idk what data type those are)'''

    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        # possibly change this
        key_size=2048
    )

    #serializes key (i think)
    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption())


    #generates public key from private key and serializes (I think)
    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PublicFormat.SubjectPublicKeyInfo
    )
    priv_key_file = name +"PrivateKey.txt"
    pub_key_file =  name +"PublicKey.txt"


    #write public key
    file = open(pub_key_file, "wb")
    file.write(public_key)
    file.close()

    #write private key file

    file = open(priv_key_file, "wb")
    file.write(private_key)
    file.close()

    return [private_key , public_key]