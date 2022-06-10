class kalkulacka:
	@classmethod
	def secti(cls,a,b):
		return a+b

	@classmethod
	def odecti(cls,a,b):
		return a-b

	@classmethod
	def nasobeni(cls,a,b):
		return a*b
	
def main():
	kalkulajda= kalkulacka()
	print(kalkulacka.secti(5,4))
	print(kalkulacka.odecti(5,44))

if __name__== "__main__":
	main()
