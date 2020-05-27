# SOMAR CADA ALGARISMO DE UMA DATA POR VEZ EM TODO ANO SELECIONADO.
# EXEMPLO:  31/10/2007 = 3 + 1 + 1 +0 + 2 + 0 + 0 + 7   = 14
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

sd, sm, sa = 0,  0, 0
sd2, sm2, sa2 = '', '', ''
t = 0
dt = ''
meses       = ['01','02','03','04','05','06','07','08','09','10','11','12']
dias        = [ "31", fev(y), "31", "30", "31", "30", "31", "31", "30", "31", "30", "31" ]
calend  = [ [],[],[],[],[],[],[],[],[],[],[],[] ]
compara = []


# REPETIR INSTRUÇÕES 12 VEZES. 
for m in meses:
    sd = int( m) - 1
    sm = int( dias[sd] )
# REPETIR INSTRUÇÕES TOTAL DE DIAS DO MÊS DA REPETIÇÃO ATUAL
    for d in range(1, sm+1):
        sa = str(d)
        if d < 10:
            sa = '0'+str(d)
        calend[sd].append(sa)


for m in meses:
    sd = int( m ) -1
    sm = int( dias[sd])
    for d in range(1, sm+1 ):
        sd2 = calend[sd][d-1]
        sm2 = dias[sd]
        dt = sd2 + '/' + m + '/' + y
        t = int( sd2[0]) + int( sd2[1]) + int( m[0]) + int( m[1]) + int( y[0]) + int( y[1]) + int( y[2]) + int( y[3])
        if t == v:
            compara.append(dt)
            print( 'Data correspondente: {}'.format(dt) )

print('')
print( 'O ano de {} tem {} dias em que a soma dos algarismos da data é igual a {} '.format(y, len(compara), v))
