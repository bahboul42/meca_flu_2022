  _____  ______          _____    __  __ ______      
 |  __ \|  ____|   /\   |  __ \  |  \/  |  ____|  _  
 | |__) | |__     /  \  | |  | | | \  / | |__    (_) 
 |  _  /|  __|   / /\ \ | |  | | | |\/| |  __|       
 | | \ \| |____ / ____ \| |__| | | |  | | |____   _  
 |_|  \_\______/_/    \_\_____/  |_|  |_|______| (_)

 ---------------------------------------------------


Informations nécessaire à l'éxécution de notre code : 
 
Veuillez suivre les étapes décrites dans le readme afin
de faciliter votre utilisation des fonctions ci-jointes.

L'appel à main se fait de cette façon :

        >> out = main(coef, show)

Où "out" est un objet comprenant les résultats utiles,
   "coef" prend une valeur correspondant au cas considéré,
   "show" prend 1 si on veut afficher les graphiques et 0 sinon.

"coef" peut prendre comme valeur :
    - 1 : Canal rectiligne (cas de base)
    - 2 : Canal avec élargissements et rétraississements brusques (Qin > 0)
    - 3 : Canal avec élargissements et rétraississements brusques (Qin < 0)
    - 4 : Ajout d'un ilot avec comme fraction de débit F = 0.5
    - 5 : Ajout d'un ilot avec comme fraction de débit F = 0.207

Voici un exemple d'appel :

        >> out = main(2,0)

        out = 

          struct with fields:

            dom: [202×52 double]
            num: [202×52 double]
             cl: [202×52 double]
            psi: [202×52 double]
              u: [202×52 double]
              v: [202×52 double]
              s: [202×52 double]
              p: [202×52 double]
          circu: 3.9774e-16
        trainee: 0.4133
       portance: -1.5987e-14
