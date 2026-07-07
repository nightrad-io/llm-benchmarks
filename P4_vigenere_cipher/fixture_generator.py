"""
P4 fixture: generates a ~520-character Vigenere ciphertext with known key
'CIPHER', deterministically, from a fixed plaintext.
"""

KEY = "CIPHER"

PLAINTEXT = """
THE OLD LIGHTHOUSE STOOD ALONE ON THE ROCKY POINT WHERE THE COLD
ATLANTIC WIND NEVER SEEMED TO REST. EVERY NIGHT THE KEEPER CLIMBED
THE WINDING IRON STAIRCASE TO LIGHT THE GREAT LANTERN BEFORE THE
LAST TRACE OF DAYLIGHT FADED FROM THE WESTERN SKY. SHIPS FAR OUT
ON THE DARK WATER DEPENDED ON THAT STEADY BEAM TO WARN THEM AWAY
FROM THE JAGGED REEF THAT HAD CLAIMED SO MANY VESSELS IN YEARS
LONG PAST. THE KEEPER HAD LIVED THERE FOR THIRTY YEARS AND KNEW
EVERY CREAK OF THE OLD TOWER AND EVERY MOOD OF THE RESTLESS SEA
BELOW. ON STORMY NIGHTS THE WAVES CRASHED AGAINST THE ROCKS WITH
A FORCE THAT SHOOK THE VERY FOUNDATIONS BUT THE LIGHT NEVER
FAILED TO TURN
""".replace("\n", " ")

# Keep only letters (A-Z), uppercase, no spaces/punctuation -- standard
# convention for classical cipher exercises.
PLAINTEXT_LETTERS = "".join(c for c in PLAINTEXT.upper() if c.isalpha())
PLAINTEXT_LETTERS = PLAINTEXT_LETTERS[:520]  # trim to target length


def vigenere_encrypt(plaintext: str, key: str) -> str:
    key = key.upper()
    out = []
    for i, c in enumerate(plaintext):
        shift = ord(key[i % len(key)]) - ord('A')
        out.append(chr((ord(c) - ord('A') + shift) % 26 + ord('A')))
    return "".join(out)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key = key.upper()
    out = []
    for i, c in enumerate(ciphertext):
        shift = ord(key[i % len(key)]) - ord('A')
        out.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
    return "".join(out)


CIPHERTEXT = vigenere_encrypt(PLAINTEXT_LETTERS, KEY)

if __name__ == "__main__":
    print(f"Plaintext length (letters only): {len(PLAINTEXT_LETTERS)}")
    print(f"Key: {KEY}")
    print()
    print("CIPHERTEXT:")
    print(CIPHERTEXT)
    print()
    # Round-trip verification
    roundtrip = vigenere_decrypt(CIPHERTEXT, KEY)
    assert roundtrip == PLAINTEXT_LETTERS, "round-trip decrypt mismatch!"
    print("Round-trip verified: decrypt(encrypt(plaintext)) == plaintext")
