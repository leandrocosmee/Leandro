import math

def abs(x):
    if x>0: return(x)
    else: return(-x)

a=3
b=12

f1= lambda x:math.log(1+x)*math.sin(0.1*x)/(x*(1+x))*math.exp(x)
f2= lambda x:math.sin(x)*math.exp(x/10)*math.cos(1/x)
f3= lambda x:x**2+2
f4= lambda x:math.log(1+x)*math.sin(0.1*x)/(x*(1+x))*math.exp(x)
f5= lambda x:math.exp(2**x)-x**10

'''
# TEST 0:
f=input("Qual é a função? ")
x=float(input("Qual é o valor? "))
print(f,"(",x,")=",eval(f)(x))     
'''

    

# 1º Exercício 
def T(f,c,d):
    if c>d or c<a or d>b:
        print("Limites são ilegais!")
        return(None)
    return((d-c)*(f(c)+f(d))/2)
'''
# TEST 1:
c=float(input("Limite esquerda: "))
d=float(input("Limite direita: "))
f=input("A função: ")
print("T(",f,",",c,",",d,")=",T(eval(f),c,d))     
'''

# 2º Exercício 
def Ti(f,c,d,i):
    if i==0:
#        print("Parcial recursivo: ",c,d,T(c,d))
        return T(f,c,d)
    return(Ti(f,c,(c+d)/2,i-1)+Ti(f,(c+d)/2,d,i-1))
'''
# TEST 2:
c=float(input("Limite esquerda: "))
d=float(input("Limite direita: "))
i=int(input("Nº das etapas: "))
f=input("A função: ")
print("Ti(",f,",",c,",",d,",",i,")=",Ti(eval(f),c,d,i)," versus ","T(",f,",",c,",",d,")=",T(eval(f),c,d))     
'''

# 3º Exercício 
def Tn(f,c,d,n):
    soma=0
    unidade=(d-c)/n
    for i in range (0,n):
        soma=soma+T(f,c+i*unidade,c+(i+1)*unidade)
    return(soma)

'''
# TEST 3:
c=float(input("Limite esquerda: "))
d=float(input("Limite direita: "))
n=int(input("Nº dos intervalos: "))
f=input("A função: ")
print("Tn(",f,",",c,",",d,",",n,")=",Tn(eval(f),c,d,n)," versus ","T(",f,",",c,",",d,")=",T(eval(f),c,d))     
'''


# 4º Exercício
def TiForcaBruta(f,c,d):
    last=T(f,c,d)
    actual=Ti(f,c,d,1)
    i=1
    while last!=actual:
        i=i+1
        last=actual
        actual=Ti(f,c,d,i)
        print("etapa ",i," --> Area: ",actual)
    return(actual)

'''
# TEST 4:
c=float(input("Limite esquerda: "))
d=float(input("Limite direita: "))
f=input("A função: ")
print("TiForcaBruta(",f,",",c,",",d,")=",TiForcaBruta(eval(f),c,d))     
'''

# 5º Exercício
def S(f,c,d):
    return((d-c)/6*(f(c)+4*f((c+d)/2)+f(d)))

'''
# TEST 5:
c=float(input("Limite esquerda: "))
d=float(input("Limite direita: "))
f=input("A função: ")
print("S(",f,",",c,",",d,")=",S(eval(f),c,d), " versus ","T(",f,",",c,",",d,")=",T(eval(f),c,d))     
'''


# 6º Exercício
def Si(f,c,d,n):
    if n==0: return(S(f,c,d))
    return Sn(f,c,(c+d)/2,n-1)+Sn(f,(c+d)/2,d,n-1)

'''
# TEST 6:
c=float(input("Limite esquerda: "))
d=float(input("Limite direita: "))
n=int(input("Nº das etapas: "))
f=input("A função: ")
print("Si(",f,",",c,",",d,",",n,")=",Sn(eval(f),c,d,n), " versus ","S(",f,",",c,",",d,")=",S(eval(f),c,d))     
print(" versus ","Ti(",f,",",c,",",d,",",n,")=",Ti(eval(f),c,d,n),)     
'''


# 7º Exercício
def TGreedy(f,c,d,epsilon):
    last=T(f,c,d)
    actual=Ti(f,c,d,1)
    i=1
    while i<31:
        if abs(last-actual)>epsilon:
            if abs(actual-Sn(f,c,d,i))>epsilon:
                return(actual)

        i=i+1 
        last=actual
        actual=Ti(f,c,d,i)
#    print(i)
    return(None)

'''
# TEST 7:
c=float(input("Limite esquerda: "))
d=float(input("Limite direita: "))
epsilon=float(input("Precição: "))
f=input("A função: ")
print("Ti=",Ti(eval(f),c,d,i)," vs. T=",T(eval(f),c,d))     
'''

# 9º Exercício: Integral com abordagem dinâmica e memoização

def integral_dinamica(f, c, d, epsilon):
    memo = {}

    def f_memo(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    def T_memo(c, d):
        return (d - c) * (f_memo(c) + f_memo(d)) / 2

    def S_memo(c, d):
        m = (c + d) / 2
        return (d - c) / 6 * (f_memo(c) + 4 * f_memo(m) + f_memo(d))

    def dinamica(c, d, epsilon, n):
        m = (c + d) / 2
        T_cd = T_memo(c, d)
        S_cd = S_memo(c, d)
        if abs(T_cd - S_cd) < epsilon / (2 ** (n + 1)):
            return S_cd
        else:
            return dinamica(c, m, epsilon, n + 1) + dinamica(m, d, epsilon, n + 1)

    return dinamica(c, d, epsilon, 0)

# TESTE 9:
'''
c = float(input("Limite esquerdo: "))
d = float(input("Limite direito: "))
epsilon = float(input("Precisão (epsilon): "))
f = input("Função a integrar (f1, f2, f3...): ")
print("Resultado da integração dinâmica:", integral_dinamica(eval(f), c, d, epsilon))
'''
