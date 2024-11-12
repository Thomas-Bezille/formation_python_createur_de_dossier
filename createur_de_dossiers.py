from pathlib import Path

path = Path("c:/xampp/htdocs/DEV/PYTHON/formation_python_createur_de_dossier/dossier_test")
folder_architecture = {
    "Film": [
        "Le seigneur des anneaux",
        "Harry Potter",
        "Moon",
        "Forest Gump",
    ],
    "Employes": [
        "Paul",
        "Pierre",
        "Marie",
    ],
    "Exercices": [
        "les_variables",
        "les_fichiers",
        "les_boucles",
    ]
}

for folder in folder_architecture.keys():
    folder_to_create_first_level = path / folder
    folder_to_create_first_level.mkdir(exist_ok=True)
    for folder in folder_architecture[folder]:
        folder_to_create_second_level = folder_to_create_first_level / folder
        folder_to_create_second_level.mkdir(exist_ok=True)