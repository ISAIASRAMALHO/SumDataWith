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


meses       = list( range(1, 13) );
dias        = [ 31, fev(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
meses_dias  = [];





for m in meses:
    for d in range(1, dias[m-1]+1 ):
        meses_dias.append(d);
        

print( meses_dias)



#print( meses );
#print('-'*20);
#print( dias );
#print('-'*20);
#print( meses_dias );
