from Crypto import Random
from Crypto.Cipher import AES
import tkinter
from tkinter import filedialog
import tkinter.messagebox

key = "12345678912345678912345678912345"

def pad(s):
	return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=265):
	message = pad(message)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext[AES.block_size:])
	return plaintext.rstrip(b"\0")

filename = None

def encrypt_file(filename, key):
	with open(filename, 'rb') as f:
		plaintext = f.read()
	enc = encrypt(plaintext, key)
	with open(filename + ".enc", 'wb') as f:
		f.write(enc)

def decrypt_file(filename, key):
	with open(filename, 'rb') as f:
		ciphertext = f.read()
	dec = decrypt(ciphertext, key)
	with open(filename[:], 'wb') as f:
		f.write(dec)

def load_file():
	global key, filename
	text_file = filedialog.askopenfile(filetypes=[('Text Files', 'txt')])
	if text_file.name != None:
		filename = text_file.name

def encrypt_the_file():
	global filename, key
	if filename != None:
		encrypt_file(filename, key)
	else:
		messagebox.showerror(title="Error:", message = "There was no file loaded to eencrypt")

def decrypt_the_file():
	global filename, key
	if filename != None:
		fname = filename + ".enc"
		decrypt_file(fname, key)
	else:
		messagebox.showerror(title="Error:", message = " There was no file loaded to decrypt")




root = tkinter.Tk()
root.title("Cryptofile")
root.minsize(width=200, height=150)
root.maxsize(width=200, height=150)

loadButton = tkinter.Button(root, text="Load Text File", command=load_file)
loadButton.grid(column = 3, row = 1, padx=50, pady=10)
encryptButton = tkinter.Button(root, text="Encrypt File", command=encrypt_the_file)
encryptButton.grid(column = 3, row= 2, padx=50, pady=10)
decryptButton = tkinter.Button(root, text="Decrypt the file", command=decrypt_the_file)
decryptButton.grid(column = 3, row = 3, padx=50, pady=10)

root.grid_columnconfigure(7, minsize=700)
#loadButton.pack()
#encryptButton.pack()
#decryptButton.pack()


root.mainloop()															