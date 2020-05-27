# PREPARANDO


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

y = input( 'Digite um ano para saber se é bisexto: ');
v = int( input('Informe o valor em que a soma e dia+mes+ano coincida: ') );

sd, sm, sa, t = 0,  0, 0, 0;
meses       = ['01','02','03','04','05','06','07','08','09','10','11','12']
dias        = [ "31", fev(y), "31", "30", "31", "30", "31", "31", "30", "31", "30", "31" ]
calend  = [ [],[],[],[],[],[],[],[],[],[],[],[] ]



# REPETIR INSTRUÇÕES 12 VEZES. 
for m in meses:
    sd = int( m) - 1
    sm = int( dias[sd] )
# REPETIR INSTRUÇÕES TOTAL DE DIAS DO MÊS DA REPETIÇÃO ATUAL
    for d in range(1, sm+1):
        calend[sd].append(d)


for c in calend:
    print( "Dias desse mês: {}".format( c ) )

    # for d in 





#print(s)        

# SOMAR CADA ALGARISMO DE UMA DATA POR VEZ EM TODO ANO SELECIONADO.
# EXEMPLO:  31/10/2007 = 3 + 1 + 1 +0 + 2 + 0 + 0 + 7   = 14