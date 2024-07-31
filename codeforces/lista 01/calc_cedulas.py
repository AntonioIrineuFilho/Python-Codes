N=int(input())
N_default=N
N100=N//100
N=N%100
N50=N//50
N=N%50  
N20=N//20
N=N%20
N10=N//10
N=N%10
N05=N//5
N=N%5
N02=N//2
N=N%2
N01=N//1
print(N_default)
print(N100,"nota(s) de R$ 100,00")
print(N50,"nota(s) de R$ 50,00")
print(N20,"nota(s) de R$ 20,00")
print(N10,"nota(s) de R$ 10,00")
print(N05,"nota(s) de R$ 5,00")
print(N02,"nota(s) de R$ 2,00")
print(N01,"nota(s) de R$ 1,00")
