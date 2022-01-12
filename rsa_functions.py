import number_theory_functions
from random import randrange

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        while(True):
            prime_num_1 = number_theory_functions.generate_prime(digits//2)
            prime_num_2 = number_theory_functions.generate_prime(digits//2)
            if((prime_num_1 is not None) and (prime_num_2 is not None)):
                break
        N = (prime_num_1) * (prime_num_2)
        phi_N = (prime_num_1-1) * (prime_num_2-1)
        num_digits = randrange(1,digits)
        while(True):
            e = number_theory_functions.generate_prime(num_digits)
            if(e is not None):
                break
        d = number_theory_functions.modular_inverse(e,phi_N)
        return RSA((N,e),(N,d))



    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        (N,e) = self.public_key
        return number_theory_functions.modular_exponent(m,e,N)


    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        (N,d) = self.private_key
        c = int(c) % int(N)
        return number_theory_functions.modular_exponent(c,d,N)