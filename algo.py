# IMPORTS
import string
import random

# FREQUENT USED VARIABLES
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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

        if letter in alphabets:
            return alphabets[new_key]
        else:
            return letter


    def encrypt(self, plaintext, key):

        message = plaintext.upper()

        ciphertext = ""

        for letter in message:

            new_key = (alphabets.find(letter) + key) % len(alphabets)

            ciphertext = ciphertext + self.get_cipherletter(new_key, letter)

        return ciphertext


    def decrypt(self, ciphertext, key):

        message = ciphertext.upper()

        plaintext = ""

        for letter in message:

            new_key = (alphabets.find(letter) - key) % len(alphabets)

            plaintext = plaintext + self.get_cipherletter(new_key, letter)

        return plaintext


    def cryptanalyse(self, ciphertext):


        for key in range(len(alphabets)):

            possibility = ""

            for letter in ciphertext:

                if letter in alphabets:

                    num = alphabets.find(letter)

                    num = num - key

                    if num < 0:

                        num = num + len(alphabets)

                    possibility = possibility + alphabets[num]

                else:

                    possibility = possibility + letter

            print(f'Key {key}: {possibility}')


class ExtendedExperimentalAPI:

    pass


class RandomPasswordGeneratorAPI:

    """
        class used to generate random passwords
        generate: takes length as an argument and prints a random password
    """

    def generate(self, length):

        if(length>=8 and length<=80):

            value = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(random.choice(value) for i in range(length))

            print(password)
        
        else:

            print('ERROR: The length of password should be in the range of 8 to 80 characters')

