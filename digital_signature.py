from lightdsa import LightDSA

# build rsa cryptosystem
dsa = LightDSA(
    algorithm_name="dsa",  # or dsa
    key_size=1024
)

# export private key
dsa.export_keys("secret.txt")

# export public key
dsa.export_keys("public.txt", public=True)


with open(r"C:\Users\kaya2\Documents\Untitled.txt", "r", encoding="utf-8") as f:
    message = f.read()

signature = dsa.sign(message)
print(signature)