#!/usr/bin/env python3
# coding: utf-8

class Blockchain(object):

	def __init__(self):
		self.current_transactions = []
		self.chain = []
		self.new_block(previous_hash=1, proof=100)

	def new_block(self, proof, previous_hash=None):
		pass

	def new_transaction(self, sender, recipient, amount):
		self.current_transactions.append({
			"sender": sender,
			"recipient": recipient,
			"amount": amount
		})
		return self.last_block["index"] + 1

	@staticmethod
	def hash(block):
		pass

	@property
	def last_block(self):
		pass

def example():
	block = {
		'index': 1,
		'timestamp': 1506057125.900785,
		'transactions': [
			{
				'sender': "8527147fe1f5426f9dd545de4b27ee00",
				'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
				'amount': 5,
			}
		],
		'proof': 324984774000,
		'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
	}

def main():

	example()
	pass

main()
