class kalkulacka:
	@classmethod
	def secti(cls,a:float,b:float) -> float:
		'''
		Tato funkce sèítá 2 funkce
		input:
			a: float
			b.float
		returns:
			float
		'''
		return a+b

	@classmethod
	def odecti(cls,a:float,b:float) -> float:
		return a-b

	@classmethod
	def nasobeni(cls,a:float,b:float) -> float:
		return a*b
	
def main():
	kalkulajda= kalkulacka()
	print(kalkulacka.secti(5,4))
	print(kalkulacka.odecti(5,44))

if __name__== "__main__":
	main()
