
 
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
	
