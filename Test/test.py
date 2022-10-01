cipher = "OVBDBXTFPIOTUIUBPOOIHBMIFOTXTEXBPOTMWNBMWJBOVBXWPSNIUUTTPSXTFCKFOWPOWUBOIVBTDWOFTENIUUTTFWOOKDPBSTNIDPBDNIUUTIVUEBTDFTPSXVWFJBDFNIUUTVIXMTOBWOFGBOOWPGFVBXTFNMIFBHBVWPSWOXVBPFVBOKDPBSOVBNIDPBDNIUUTHKOOVBDTHHWOXTFPIMIPGBDOIHBFBBPFVBRIKPSVBDFBMRWPTMIPGNIUUTMIXVTMMNIUUTXVWNVXTFMWOKLHETDIXIRMTULFVTPGWPGRDIUOVBDIIRSIOOVBDBXBDBSIIDFTMMDIKPSOVBVTMMNIUUTHKOOVBEXBDBTMMMINJBSTPSXVBPTMWNBVTSHBBPTMMOVBXTESIXPIPBFWSBTPSKLOVBIOVBDNIUUTODEWPGBABDESIIDNIUUTFVBXTMJBSFTSMESIXPOVBUWSSMBNIUUTXIPSBDWPGVIXFVBXTFBABDOIGBOIKOTGTWP"
cipher_lower = cipher.lower()
test_plaintext_1 = "abcde"
test_plaintext_2 = "qwer"
test_ciphertext_1 = ""
cipher1 = "OVBIOT"

import string

my_alphas = string.ascii_lowercase  # string of lowercase alphabates


# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))


# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))


# print(cipher_lower)
# print(cipherText(test_plaintext_1, 1))
# print(originalText(test_plaintext_2, 3))
# print(ascii_caesar_shift(cipher_lower, 3))

# print(ord('a'))
# print(ord('z'))


def decodeMonoalphabetic(string):
    shift = 1
    for i in string:
        num = (ord(i) - ord('a') + 1) % 26
        char = chr(num + shift + ord('a') - 1)
        print(i + " " + char)

# test
decodeMonoalphabetic("abcdefghijklmnopqrstuvwxyz")




