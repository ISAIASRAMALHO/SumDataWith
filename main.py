# PREPARANDO


def AnoBisexto( ano ):
    i_ano = int(ano)
    if i_ano % 4 == 0:
        if i_ano % 100 != 0:
            fev = 29;
        else:
            fev = 28;
    else:
        fev = 28;  
    return fev;


def fev( ano ):
    return AnoBisexto( ano);

y = input( 'Digite um ano para saber se é bisexto: ');
v = int( input('Informe o valor em que a soma e dia+mes+ano coincida: ') );

s, t = 0, 0;
meses       = list( range(1, 13) )
dias        = [ 31, fev(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses_dias  = [ [],[],[],[],[],[],[],[],[],[],[],[] ]


for m in meses:
    for d in range(1, dias[m-1]+1 ):
        meses_dias[m-1].append(d)
        print('{}/{}/{}'.format(d, m, y))
        s = s+1
    


print(s)        

# SOMAR CADA DATA DO CALENDARIO DO ANO SELECIONADO.

#for m in meses:
#    for d in range(1, meses_dias[m] ):
#        s = d + m + int(y);
#        if s == v:
#            t=t+1;


