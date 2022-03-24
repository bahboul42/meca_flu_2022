*******************************************************************
** Instructions pour l'utilisation des fichiers d'initialisation **
*******************************************************************


Conseils pour importer les fichiers dans Python:
------------------------------------------------

Utiliser la commande numpy.loadtxt.
ex: my_matrix = numpy.loadtxt('my_file.txt')
Vous pouvez �galement pr�ciser que les donn�es lues sont d'un certain type.
ex: my_matrix = numpy.loadtxt('my_file.txt', dtype = int)

La pas de discr�tisation est pr�cis� ci-dessous.


Conventions:
------------

Pour chaque cas � faire passer, 2 ou 3 matrices sont fournies:
	1) Dans tous les cas: une matrice repr�sentant le domaine g�om�trique (appel�e dom)
	Elle permet d'identifier
		1) Les noeuds qui ne doivent pas �tre calcul�s (valeur de 0). Une frange de 0 est plac�e
		autour de chaque domaine.
		2) Les noeuds internes prennent une valeur = 1.
		3) Les noeuds condition limite de Dirichlet sont rep�r�s par une valeur de 2.
		
    	2) Dans tous les cas: une matrice qui donne un num�ro de noeud pour chaque noeud de calcul (appel�e num). Cette num�rotation permet d'ordonner le syst�me � r�soudre. Pour plus d'infos, voir la s�ance introductive ou avec les �tudiants-moniteurs.

	3) Pour le canal rectiligne (cas test): une matrice reprenant les valeurs des conditions de Dirichlet (appel�e cl)
	
Informations compl�mentaires:
-----------------------------

1) Canal rectiligne - pas spatial = 0.5 m

2) Canal avec �largissement et r�tr�cissement - pas spatial = 0.01 m

3) Cas 2) avec �lot - pas spatial = 0.01 m (!attention! 2 CL de Dirichlet � tester)
