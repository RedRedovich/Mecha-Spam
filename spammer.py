from pyrogram import Client
from colorama import Fore, init
import os
import sys
import time
import random
os.system("cls")
init()

magenta = Fore.MAGENTA
cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
print(f"""
			{magenta}Mecha Spam

		{cyan}version: 1.0.0
		author: @Redpiar

		{magenta}links:
		channel: https://t.me/BotesForTelegram

		{red}CopyRight: @Redpiar
""")
dirname = os.path.dirname(__file__)

channel = open(f"{dirname}/needed_files/channel.txt")
channel_load = channel.read().split(" ")

accounts = open(f"{dirname}/needed_files/accounts.txt")
acc_load = accounts.read().split(" ")

message = open(f"{dirname}/needed_files/message.txt")
message_load = message.read().split("<n>")

for i in range(0, 100000):
	try:
		message_load[i]
	except IndexError:
		a = i
		print(f"{green}>> loaded {i} messages\n")
		break
class tg:
	def __init__(self):
		global a
		self.colors = {
			"RED": Fore.RED,
			"MAGENTA": Fore.MAGENTA,
			"CYAN": Fore.CYAN,
			"GREEN": Fore.GREEN,
			"WHITE": Fore.WHITE
		}

		self.accounts = 2
		self.start = True
		self.error = 0
		self.maxmessage = a


	def classic_spam(self):
		api_id = acc_load[0]
		api_hash = acc_load[1]
		phone = acc_load[self.accounts]

		app = Client(phone, api_id=api_id, api_hash=api_hash)
		app.connect()

		try:
			app.send_message('me', "connect")
			print(f"{self.colors['CYAN']}connect in {phone}{self.colors['WHITE']}")
		except:
			code_hash = app.send_code(phone)
			print(f"{phone}")
			code = input("Enter Code: ")
			app.sign_in(phone, code_hash.phone_code_hash, code)
			print("log")
			app.send_message('me', "connect")
			app.disconnect()
		try:
			app.connect()
		except:
			pass

		col_vo = input("Enter number of messages: ")
		end = 0

		try:
			app.join_chat(channel_load[0])
			print(f"{self.colors['GREEN']}>> join in {channel_load[0]}!{self.colors['WHITE']}")
		except:
			print(f"{self.colors['RED']}[!] Error join in {channel_load[0]}!{self.colors['WHITE']}")
			pass

		while self.start:
			if end == int(col_vo):
				self.start = False

			try:
				app.send_message(channel_load[0], message_load[random.randint(0, self.maxmessage)])
				print(f"{self.colors['GREEN']}>> send message in {channel_load[0]}!{self.colors['WHITE']}")
			except:
				print(f"{self.colors['RED']}[!] error send message in {channel_load[0]}!{self.colors['WHITE']}")
				pass

			end = end + 1



	def hard_spam(self):
		api_id = acc_load[0]
		api_hash = acc_load[1]

		col_vo = input("Enter number of messages per account: ")

		message_per_accounts = 0

		while self.start:
			try:
				phone = acc_load[self.accounts]
			except IndexError:
				self.accounts = 2
				phone = acc_load[self.accounts]

			app = Client(phone, api_id=api_id, api_hash=api_hash)
			app.connect()

			try:
				app.send_message('me', "connect")
				print(f"{self.colors['CYAN']}connect in {phone}{self.colors['WHITE']}")
			except:
				print(f"{self.colors['RED']}[Error accounts] you registered accounts?{self.colors['WHITE']}")
				sys.exit()

			try:
				app.join_chat(channel_load[0])
			except:
				pass

			while True:
				if message_per_accounts == int(col_vo):
					self.accounts = self.accounts + 1
					message_per_accounts = 0
					app.disconnect()
					break

				try:
					app.send_message(channel_load[0], message_load[random.randint(0, self.maxmessage)])
					print(f"{self.colors['GREEN']}>> send message in {channel_load[0]}!{self.colors['WHITE']}")
					message_per_accounts = message_per_accounts + 1
				except:
					print(f"{self.colors['RED']}[!] error send message in {channel_load[0]}!{self.colors['WHITE']}")
					self.error = self.error + 1
					if self.error == 5:
						message_per_accounts = 0
						self.accounts = self.accounts + 1
						self.error = self.error * 0
						app.disconnect()
						break
					pass





	def reg(self):
		api_id = acc_load[0]
		api_hash = acc_load[1]

		while True:

			try:
				phone = acc_load[self.accounts]
			except IndexError:
				print("all accounts reg")
				break

			app = Client(f"{dirname}/accounts_files/{phone}", api_id=api_id, api_hash=api_hash)
			app.connect()

			try:
				app.send_message('me', "connect")
				print(f"{self.colors['CYAN']}connect in {phone}{self.colors['WHITE']}")
			except:
				code_hash = app.send_code(phone)
				print(f"code send in {phone}")
				code = input("Enter Code: ")
				app.sign_in(phone, code_hash.phone_code_hash, code)
				print("log")
				app.send_message('me', "connect")
				app.disconnect()

	def load(self):
		print(f"{self.colors['MAGENTA']}1. classic spam\n2. Mega spam\n3. register")
		selected = input("Enter the number(1-3): ")

		if selected == "1":
			tg().classic_spam()

		if selected == "2":
			tg().hard_spam()

		if selected == "3":
			tg().reg()

tg().load()