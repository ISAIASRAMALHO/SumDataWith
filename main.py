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


y = input( 'Digite um ano para saber se é bisexto: ');


meses       = list( range(1,13));
dias        = [ 31, AnoBisexto(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
meses_dias  = [ [],[],[],[],[],[],[],[],[],[],[],[] ];




for m in meses:
    for d in range(dias[m]):
        meses_dias[m] = d;


print( meses );
print( dias );
print( meses_dias );
