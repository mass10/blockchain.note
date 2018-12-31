#!/usr/bin/env python3

import json
import hashlib

class util:

	@staticmethod
	def hash(block):

		s = json.dumps(block, ensure_ascii=False)
		s = s.encode("utf-8")
		g = hashlib.md5()
		g.update(s)
		return g.hexdigest()

class blockchain:

	def __init__(self):

		self.new_element = {"data": {"name": "", "email": ""}, "hash": ""}
		self.chain = []
		self.chain.append(self.new_element)

	def new_block(self, unknown):

		new_element = unknown.copy()
		new_element["hash"] = util.hash(self.new_element)
		self.chain.append(new_element)
		self.new_element = new_element

	def verify(self):

		last_chain = None
		for e in self.chain:
			if last_chain == None:
				last_chain = e
				continue
			last_hash = util.hash(last_chain)
			this_hash = e["hash"]
			print("[TRACE] ", e["hash"], ": ", last_hash == this_hash, sep="")
			last_chain = e

	def dump(self):

		print("### dump ###")
		print(json.dumps(self.chain, ensure_ascii=False, indent=4, sort_keys=True))

def main():

	chain = blockchain()
	chain.new_block({"data": {"name": "Jimi Hendrix", "email": "jimi.hendrix@docomo.ne.jp"}})
	chain.new_block({"data": {"name": "Freddie Mercury", "email": "farrokh.bulsara@gmail.com"}})
	chain.verify()
	chain.dump()

main()
