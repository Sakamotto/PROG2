'''
Nome: Danilo de Oliveira;
Turma: BSI 2014/2;
Data: 14-04-2015;
Professor: Ernani;

Exercícios: Biblioteca_Processamento_de_TEXTO.

'''



 
def corrente(ptexto,pposicao):
	separadores = ' ,.:!?;'
	
	if pposicao <0 or pposicao>=len(ptexto):
		return None
	
	else:
		if ptexto[pposicao] in separadores:
			return None
		
		else:
			i = pposicao
			j = pposicao
			while i>=0 and ptexto[i] != ' ':
				i-=1
			
			i+=1
			
			while ptexto[j] not in separadores and j<len(ptexto):
				j+=1
			
			return ptexto[i:j]
			
def anterior(ptexto,pposicao):
	separadores = ' ,.:;!' ; i = 0
	
	if pposicao <0 or pposicao>=len(ptexto):
		return None
	
	else:
		i = pposicao 
		
		while ptexto[i] != ' ' and i>=0:
			if i==0:
				return None
			i-=1
		
		while ptexto[i] in separadores:
			i-=1
		
		return corrente(ptexto,i)		

	
def proxima(ptexto,pposicao):
	separadores = ' ,.:;!' ; i = 0
	
	if pposicao <0 or pposicao>=len(ptexto):
		return None
	
	else:
		i = pposicao 
		
		while ptexto[i] != ' ' and i>=0:
			if i==0:
				return None
			i+=1
		
		while ptexto[i] in separadores:
			i+=1
		
		return corrente(ptexto,i)		
	
	
def separaPal(texto):
	separadores = '-/\|_+={}[]@#$%*().!?:;, ' ; palavras = [] ; i = ''
	palavra = ''
	
	texto = texto+'.' #Caso o usuário nao digite um ponto final, coloco este ponto final para saber onde termina a ultima palvra.
	
	
	for i in texto: #i recebera cada caracter do texto digitado.
		
		if i not in separadores: # confere se o caracter i está contido na string que contem os separadores.
			palavra = palavra+i
		
		else:
			if len(palavra)>=1: # Isso evita que ele adicione a lista de palavras uma string vazia.
				palavras.append(palavra)
			palavra = ''
		
	
	return palavras



def imprimeFreq(dicionario):
	
	for i in dicionario:
		print(i, ':', dicionario[i])
	
	
	return 0
	
	
def geratabfreq(ptexto):
	dicFreqPalav = {}
	lstPalavras = separaPal(ptexto)
	
	for i in range(len(lstPalavras)):
		if lstPalavras[i].lower() not in list(dicFreqPalav.keys()):
			dicFreqPalav[lstPalavras[i].lower()] = 1
			j=i+1
			
			while j<len(lstPalavras):
				if lstPalavras[i].lower() == lstPalavras[j].lower():
					dicFreqPalav[lstPalavras[i].lower()] +=1
				
				j+=1
	
	imprimeFreq(dicFreqPalav)
	
	
	return 0
	

def eliminaPR(t1):
	listaPalavras = [] ; palavras = [] ; i = 0
	
	palavras = separaPal(t1)
	
	for i in range(len(palavras)):
		if palavras[i] not in listaPalavras:
			listaPalavras.append(palavras[i])
	
	
	
	
	return listaPalavras


def intersec(t1,t2):
	conjTexto1 = [] ; i = 0 
	
	conjTexto1 = eliminaPR(t1)
	
	while i<len(conjTexto1):
		if conjTexto1[i] not in t2:
			del conjTexto1[i]
		else:
			i+=1
	
	
	return conjTexto1

def n_grama(ptexto,ptam):
	ngrama = [] ; i = 0
	
	for i in range(len(ptexto)-ptam+1):
		ngrama.append(ptexto[i:i+ptam])
	
	return ngrama


def uniao(txt1,txt2):
	cjUniao = [] ; t1 = [] ; t2 = [] ; palavra = ''
	
	t1 = eliminaPR(txt1)
	t2 = eliminaPR(txt2)
	
	for palavra in t1:
		cjUniao.append(palavra)
	
	for palavra in t2:
		if palavra not in cjUniao:
			cjUniao.append(palavra)	
	
	return cjUniao
	


def removeAcentos(ptexto):
	acentuados = 'ẃéŕýúíóṕáśǵḱĺḉźǘńḿŵêŷûîôâŝĝĥĵẑĉẁèỳùìòàǜǹẽỹũĩõãṽñ' ; equivalentes = 'weryuiopasgklçzunmweyuioasghjzcweyuioauneyuioavn' ; caracter = '' ; newTexto = '' ; palavra = '' ; j = 0
	
	for i in range(len(ptexto)):
		j=0
		caracter = ptexto[i].lower()
		while j<len(acentuados) and caracter!=acentuados[j]:
			j+=1 
		
		if j==len(acentuados):
			newTexto+=ptexto[i]
		else:
			if ptexto[i] == caracter:
				newTexto+=equivalentes[j]
			else:
				newTexto+=equivalentes[j].upper()
		
	
	return newTexto

def ehromano(ptexto):
	romanos = 'IVXLCDM'
	
	for i in ptexto:
		if i not in romanos:
			return False
	
	return True


def contadorRomanos():
	m = '' ; c = '' ; d = '' ; u = '';
	
	romanos = 'IVXLCDM' ; numero = ''
	unidade = ['','I','II','III','IV','V','VI','VII','VIII','IX']
	dezena 	= ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
	centena = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
	milhar  = ['','M','MM']
	
	for m in milhar:
		for c in centena:
			for d in dezena:
				for u in unidade:
					numero = m+c+d+u
					if numero!='':
						print(numero)
					
	
	print('MMM')
	
	return 0
	
def tokenizador(ptxt):
	tokens = [] ; lstposicoes = [] ; texto = '' ; strbuffer = '' ; posicao = 0 ; p = 0
	
	texto = insereEspacos(ptxt)
	separad = Separadores(texto)
	
	
	while posicao < len(texto):
		if texto[posicao] not in separad:
			strbuffer+=texto[posicao]
			
		else:
			if strbuffer!='':
				tokens.append(strbuffer)
				strbuffer=''
			if texto[posicao] != ' ':
				tokens.append(texto[posicao])
		posicao+=1
	
	return tokens,lstposicoes



def codifica(ptexto):
	dicTipos = {0:['de','da','do','das','dos','ao','às','aos','à','dum','duma','duns','dumas','no','na','nos','nas','num','numa','nuns','numas','por','pelo','pela','pelos','pelas'],1:['o','a','os','as','um','uns','uma','umas'],3:'1234567890',2:['e','nem','mas também','como também','bem como','mas','porém','todavia','contudo','logo','portanto','por conseguinte','que','porque','porquanto','pois']} ; count=0
	codigos = ['p','a','c','N','M','m']
	txtCodificado = ''
	tokens=tokenizador(ptexto)[0]
	dicTiposMm= {4:'QWERTYUIOPASDFGHJKLÇZXCVBNM',5:'qwertyuiopasdfghjklçzxcvbnm'}
	numBuffer = ''
	separador = True
	chave = 0
	

	if len(tokens)==0:
		return ''
	
	for i in tokens:
		chave = 0
		separador = True
		while chave < 3:
			if i.lower() in dicTipos[chave]:
				txtCodificado+=codigos[chave]
				separador = False		
			
			chave+=1
		
		if i[0] in dicTipos[chave]:
			txtCodificado += 'N'
			separador = False
		chave+=1
		
		while chave < 6 and separador == True:
			if i[0] in dicTiposMm[chave]:
				txtCodificado += codigos[chave]
				separador = False
			chave+=1
		
		if separador == True:
			txtCodificado+=i
		
	
	return txtCodificado


def Separadores(strTexto):
	lstSeparadores = ''
	
	for i in strTexto:
		teste = i.isdigit() or i.isupper() or i.islower()
		if not teste:
			lstSeparadores+=i
	
	return lstSeparadores

def insereEspacos(strTexto):
	newTexto = '' ; strbuffer='' ; separadores = ''
	
	separadores = Separadores(strTexto)
	
	if len(strTexto)>0:
		for caracter in strTexto:
			if caracter not in separadores:
				newTexto+=caracter
			else:
				newTexto+=' '+caracter+' '
			
	return newTexto


def extraiPadroes(plista):
	lstPalavras = [] ; entidade = '' ; p = 0 ; indice = 0
	textoCodificado=''
	listaP = ['MM','M','MMpM','N/N/N','MpM','MMM','MMMM','MMpMM','MpMM','MMMpM','MMMpMM','MMpMMM']
	
	listaT = plista[:]
	for i in listaT:
		textoCodificado+=codifica(i)
		print(codifica(i))
	
	print(textoCodificado)
	a=input('Fim.')
	return lstPalavras


# Manipulação de arquivos.
def copia(parqO,parqC):
	arqO = open(parqO,'rt')
	arqC = open(parqC,'wt')
	
	arqC.write(arqO.read())
	
	arqO.close()
	arqC.close()	
	
	return 0


def BDD_Separadores(arquivo):
	lstSeparadores = [] ; condicao = True
	
	arq = open(arquivo,'rt')
	separadores = open('/home/danilo/Documentos/Separadores.txt','wt')
	
	
	for linha in arq.readlines():
		for caracter in linha:
			condicao = caracter.isupper() or caracter.islower() or caracter.isdigit()
			if not condicao and caracter.lower() not in lstSeparadores:
				lstSeparadores.append(caracter)
			
	
	separadores.write(str(lstSeparadores))
	
	arq.close()
	separadores.close()	
	
	return lstSeparadores

def separaPalavras2(ptexto,psep):
	palavras = [] ; strbuffer = ''
	
	for i in ptexto:
		if i not in psep:
			strbuffer+=i
		else:
			if strbuffer!='':
				palavras.append(strbuffer)
			strbuffer=''
	
	return palavras




def geratabFreq02(arqE,arqS):
	frequencia = {} ; PalavrasP = []
	
	diretorio = arqE
	
	arquivo = open(diretorio,'rt')
	arqFreq = open(arqS,'wt')
	
	PalavrasP = extraiPadroes(tokenizador(arquivo.read()))
	
	print(PalavrasP)
	
	
	
	arqFreq.close()
	arquivo.close()
	
	
	return 0


def concatenaArq(lstArquivos,arqS):
	
	
	
	return 0




def main():
	
	diretorio = '/home/danilo/Documentos/'
	
	'''geratabFreq02(diretorio+'arquivo1Original.txt',diretorio+'CopiaArquivo1.txt')
	'''
	arquivo = open(diretorio+'arquivo1Original.txt','rt')
	arquivo.seek(0)
	print(extraiPadroes(tokenizador(arquivo.read())[0]))
	arquivo.close()
	
	''''''
	return 0

if __name__ == '__main__':
	main()
