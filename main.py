# SOMAR CADA ALGARISMO DE UMA DATA POR VEZ EM TODO ANO SELECIONADO.
# EXEMPLO:  31/10/2007 = 3 + 1 + 1 +0 + 2 + 0 + 0 + 7   = 14
# PREPARANDO

from datetime import datetime

def AnoBisexto( ano ):
    i_ano = int(ano)
    if i_ano % 4 == 0:
        if i_ano % 100 != 0:
            fev = "29";
        else:
            fev = "28";
    else:
        fev = "28";  
    return fev;


def fev( ano ):
    return AnoBisexto( ano);

a = input( 'Digite um ano para saber se é bisexto: ');
v = int( input('Informe o valor em que a soma e dia+mes+ano coincida: ') );

sm = 0
ano_atual = datetime.today().year

# REFATORANDO PARTE DO CÓDIGO USANDO DICIONARIO

meses       = ['01','02','03','04','05','06','07','08','09','10','11','12']
dias        = [ "31", fev(a), "31", "30", "31", "30", "31", "31", "30", "31", "30", "31" ]
calend  = {}
compara = []


# REPETIR INSTRUÇÕES 12 VEZES. 
for m in meses:
    calend[m] = [ v for v in range(1, int( dias[ int(m)-1 ] ) +1   )]
    # LOOP DOS DIAS
    for d in range(1, len( calend[ m ] ) + 1 ):
        sm = d + int( m[0] )+ int( m[1]) + int( a[0]) +int( a[1]) +int( a[2]) +int( a[3])
        datando = str(d)  + '/' + m + '/' + a
        if d < 10:
            datando = '0'+datando
        if sm == v:
            compara.append(datando )
        print(compara)


print('')
if int(a) < ano_atual:
    conjunga_tem = 'tinha'
elif int(a) > ano_atual:
    conjunga_tem = 'terá'
else:
    conjunga_tem = 'tem'

print( 'O ano de {} {} {} dias em que a soma dos algarismos da data é igual a {} '.format(a, conjunga_tem, len(compara), v))