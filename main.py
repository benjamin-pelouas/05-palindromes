def ispalindrome(s: str) -> bool:
    """
    Vérifie si une chaîne 's' est un palindrome.

    La vérification ignore la casse, les espaces, la ponctuation et
    les accents.

    Args:
        s: La chaîne de caractères à tester.

    Returns:
        True si 's' est un palindrome, False sinon.
    """

    # On définit les caractères à remplacer et par quoi les remplacer.
    accents_in = "áàâäéèêëíìîïóòôöúùûüç"
    accents_out = "aaaaeeeeiiiioooouuuuc"

    # str.maketrans crée la "carte" de remplacement
    translation_table = str.maketrans(accents_in, accents_out)


    # On met tout en minuscule et on enlève les accents
    s_normalized = s.lower().translate(translation_table)

    # On ne garde que les caractères alphanumériques (lettres et chiffres)
    # On filtre les espaces, virgules, points, etc.
    s_cleaned = "".join(char for char in s_normalized if char.isalnum())


    # On compare la chaîne nettoyée avec son inverse.
    # s_cleaned[::-1] est une "slice" qui inverse la chaîne.
    return s_cleaned == s_cleaned[::-1]


def main():
    """
    Fonction principale pour tester la fonction secondaire ispalindrome().
    """
    print("--- Tests de la fonction ispalindrome ---")

    test_cases = [
        "kayak",  # Simple, Attendu: True
        "ressasser",  # Simple, Attendu: True
        "bonjour",  # Simple, Attendu: False
        "Radar",  # Casse, Attendu: True
        "Élu par cette crapule",  # Accents + Casse, Attendu: True
        "Esope reste ici et se repose.",  # Ponctuation + Espaces, Attendu: True
        "Non",  # Non-palindrome, Attendu: False
        "Engage le jeu, que je le gagne."  # Complexe, Attendu: True
    ]

    for test_str in test_cases:
        print(f"'{test_str}' : {ispalindrome(test_str)}")


if __name__ == "__main__":
    main()
