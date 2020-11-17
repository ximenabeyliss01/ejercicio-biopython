from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os
filename= os.path.abspath("data/opuntia.fasta")
#Creacion de funcion
def summarize_contents(filename):
	File_List = []
	File_Extension = []
	
	File_List = os.path.split(filename)
	File_Extension = os.path.splitext(filename)
	
	if(File_Extension[1] == ".gbk"):
		type_file= "genbank"
	else:
		type_file= "fasta"
		
	record = list(SeqIO.parse(filename, type_file))
	
	d={}
	d['File:'] = File_List[1]
	d['Path:'] = File_List[0]
	d['Num_Records:'] = len(record)

	d['Names:'] = []
	d['IDs:'] = []
	d['Descriptions: '] = []
	
	
	for seq_record in SeqIO.parse(filename, type_file):
		d['Names:'].append(seq_record.name)
		d['IDs:'].append(seq_record.id)
		d['Descriptions: '].append(seq_record.description)
	return d

if __name__ == "__main__":
	resultado = summarize_contents(filename)
	print (resultado) 	
summarize_contents(filename)

#Secuencia ingresada por el usuario
	entrada1  =  input ( "Ingresar la primera secuencia de ADN:" )
	entrada2  =  input ( "Ingresar la segunda secuencia de ADN:" )

	Secuencia1  = ( entrada1 )
	Secuencia2  = ( entrada2 )

# Función definida
#Se determina la función ya que la secuencia es insertada

def  concatenate_and_get_reverse_of_complement ( Secuencia1 , Secuencia2 ):
	concatenate  =  Sequence1  +  Sequence2  #serie de cadenas
	invers  =  concatenar . complemento_inverso ())
	return ( concatenar . reverse_complement ())

if  __name__  ==  "__main__" :
	ressequence2  =  concatenate_and_get_reverse_of_complement ( Secuencia1 , Secuencia2 )
	imprimir ( ressequence2 )
== == == =
secuencia  =  'AGCTATACGACTCAG'
def  print_protein_and_stop_codon_using_standard_table ( secuencia ):
	prueba :
		cadena  =  Seq ( secuencia )
	excepto :
		return ( "Cadena no correspondiente a secuencia de nucelótidos" )
	Diccionario  = {}
	SecuenciaRNA  =  cadena . transcribir ()
	Diccionario [ 'RNAm:' ] =  SecuenciaRNA
	Diccionario [ 'Protein:' ] = []
	cinicio  =  Falso
	para el  codón  en el  rango ( 0 , len ( secuencia ), 3 ):
		si  "GCT"  o  "ATG"  o  "TTG"  en  secuencia [ codón : codón + 3 ]:
			stcodon  =  codón
			DNAcodon  =  Seq ( secuencia [ codon : len ( cadena )])

			Diccionario [ 'Proteina:' ]. añadir ( codDNA . traducir ( tabla  =  1 ))
			cinicio  =  Verdadero
			romper

	si  cinicio  ==  Falso :
		raise  TypeError ( "No se presentan tripletes y / o codones de inicio en la secuencia" )

	Diccionario [ 'Stop Codon' ] = []
	si  cinicio  ==  Verdadero :
		para el  codón  en el  rango ( 0 , len ( secuencia ), 3 ):
			si ( 'AAT'  en  secuencia [ codon : codon + 3 ]) y ( stcodon  <  codon ):
				Diccionario [ 'codón de parada' ]. añadir ( 'AAT' )
				romper
			si ( 'GCT'  en  secuencia [ codon : codon + 3 ]) y ( stcodon  <  codon ):
				Diccionario [ 'codón de parada' ]. añadir ( 'GCT' )
				romper
			if ( 'CTA'  en  secuencia [ codon : codon + 3 ]) y ( stcodon  <  codon ):
				Diccionario [ 'codón de parada' ]. añadir ( 'CTA' )
				romper

	volver  Diccionario

if  __name__  ==  "__main__" :
	resultado  =  print_protein_and_stop_codon_using_standard_table ( secuencia )
	imprimir ( resultado )
