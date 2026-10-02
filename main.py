"""Exemple d'utilisation de la classe Noeud."""

from noeud import Noeud

# Construction de l'expression exp(2 + y)
deux = Noeud(2)
y = Noeud("y")
somme = Noeud("+")
somme.ajouter_enfant(deux)
somme.ajouter_enfant(y)
expression = Noeud("exp")
expression.ajouter_enfant(somme)

# Vérification de l'affichage en notation polonaise
print(expression.afficher_polonaise())  # exp + 2 y

# Exemple d'évaluation : exp(2 + 1) = exp(3)
print(expression.evaluer({"y": 1}))

# Exemple de tracé en faisant varier y
expression.tracer("y", [-2, -1, 0, 1, 2])