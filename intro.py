from string import ascii_lowercase, digits, punctuation
fusion = ascii_lowercase + digits + punctuation

#Securing Accounts
'''
Gabungan antara ascii, digit atau angka dan tanda baca dalam pass 
menjadikan pass tidak mudah ditebak. Komputer dapat menebak pass tersebut
dengan berdasarkan kompleksitas yang rumit. Contoh dibawah ini :
4 digits, miliseconds
4 fusion, about 3 minutes

social engineering, 
phishing, gathering by faking or impersonating page or other forms
single sign on (SSO),

1:03:25
use of password managers
'''
for i in fusion:
    for j in fusion:
        for k in fusion:
            for l in fusion:
                print(i, j, k, l)

#Securing Data
'''
Hashing, password and converting it to hash value
    ex : sha-224/256/384/(512|224)/(512|256)
         sha3-224/256/384/512
rainbow tables, 
salting, to make hashing a little bit different. ex, if 2 or more person have the same pass, it would be still different
depend on, industry, country, and regulatory environment
encode, plaintext to codetext
decode, codetext to plaintext
ciphers, algorithmic
encrypt - decrypt
secret-key cryptography
DSA
ECDSA
RSA, c = m(e) mod n
     m = c(d) mod n
Diffie-Hellman, s = b(a) mod p
                s = a(b) mod p
'''

#Securing systems
'''
'''

#Securing software
'''
stored attack, 
character escapes, removing dangerous character (&lt(<); &gt(>); &amp(&); &quot(""); &apos('')
use of style-src instead of <script src="..."></script>
JSX, javascript and html combination. would have to use an external file
sql injection, in databases. ans prepared answers
command injection
'''

'''
Arbitrary code execution (ACE)
Remote code execution (RCE)
buffer overflow
'''

