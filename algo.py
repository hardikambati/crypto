# IMPORTS
from os import name
import string
import random
from PIL import Image
from Crypto.Cipher import AES

# FREQUENT USED VARIABLES

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class CaesarAPI:

    """
        consists of 3 methods:
        Encrypt: Used to encrypt a plaintext by passing plaintext and key as arguments [returns a ciphertext]
        Decrypt: Used to decrypt a ciphertext by passing ciphertext and key as arguments [returns a plaintext]
        Cryptanalyse: Used to print 25 possibilities of the given ciphertext by using brute force

        get_cipherletter: helper function
    """

    @staticmethod
    def get_cipherletter(new_key, letter):

        if letter in ALPHABET:
            return ALPHABET[new_key]
        else:
            return letter

    def encrypt(self, plaintext, key):

        message = plaintext.upper()

        ciphertext = ""

        for letter in message:

            new_key = (ALPHABET.find(letter) + key) % len(ALPHABET)

            ciphertext = ciphertext + self.get_cipherletter(new_key, letter)

        return ciphertext

    def decrypt(self, ciphertext, key):

        message = ciphertext.upper()

        plaintext = ""

        for letter in message:

            new_key = (ALPHABET.find(letter) - key) % len(ALPHABET)

            plaintext = plaintext + self.get_cipherletter(new_key, letter)

        return plaintext

    def cryptanalyse(self, ciphertext):

        for key in range(len(ALPHABET)):

            possibility = ""

            for letter in ciphertext:

                if letter in ALPHABET:

                    num = ALPHABET.find(letter)

                    num = num - key

                    if num < 0:

                        num = num + len(ALPHABET)

                    possibility = possibility + ALPHABET[num]

                else:

                    possibility = possibility + letter

            print(f'Key {key}: {possibility}')


class ExtendedExperimentalAPI:

    def __init__(self, image_path):
        self.KEY = "770A8A65DA156D24EE2A093277530142"
        self.image = Image.open(image_path)
        self.data = None

    def generate_message(self):
        data = self.image.convert("RGB").tobytes()
        original = len(data)
        data = data + b"\x00" * (16 - len(data) % 16)
        self.data = data[:original]

    def encrypt(self, aes, filename):
        new_data = aes.encrypt(self.data)
        r, g, b = tuple(
            map(lambda d: [new_data[i] for i in range(0, len(new_data)) if i % 3 == d], [0, 1, 2]))
        pixels = tuple(zip(r, g, b))
        im2 = Image.new(self.image.mode, self.image.size)
        im2.putdata(pixels)
        im2.save(f"{filename}.BMP", "BMP")

    def ecb(self):
        self.generate_message()
        aes = AES.new(self.KEY.encode('utf-8'), AES.MODE_ECB)
        self.encrypt(aes=aes, filename="ecb")

    def cbc(self):
        self.generate_message()
        IV = "A"*16
        aes = AES.new(self.KEY.encode('utf-8'), AES.MODE_CBC, IV.encode('utf-8'))
        self.encrypt(aes=aes, filename="cbc")

    def cfb(self):
        self.generate_message()
        IV = "A"*16
        aes = AES.new(self.KEY.encode('utf-8'), AES.MODE_CFB, IV.encode('utf-8'))
        self.encrypt(aes=aes, filename="cfb")


class RandomPasswordGeneratorAPI:

    """
        class used to generate random passwords
        generate: takes length as an argument and prints a random password
    """

    def generate(self, length):

        if(length >= 8 and length <= 80):

            value = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(random.choice(value) for i in range(length))

            print(password)

        else:

            print(
                'ERROR: The length of password should be in the range of 8 to 80 characters')


def driver():

    # assingment1 = CaesarAPI()
    # cipher_text = assingment1.encrypt("Hello World", "1qaz2wsx")
    # print(cipher_text)
    # plain_text = assingment1.decrypt(cipher_text, "1qaz2wsx")
    # print(plain_text)
    # cryptanalyze = assingment1.cryptanalyse(cipher_text)
    # print(cryptanalyze)

    assingment2 = ExtendedExperimentalAPI("Linux-icon.bmp")
    assingment2.ecb()
    assingment2.cbc()
    assingment2.cfb()

    # assingment3 = RandomPasswordGeneratorAPI()
    # assingment3.generate(12)

if __name__ == "__main__":
    driver()
