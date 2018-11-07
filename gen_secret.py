import binascii
import os


if __name__ == '__main__':
    print(binascii.hexlify(os.urandom(24)))
