# Importation des modules nécessaires
import numpy as np
import csv

# Définition de la liste des actions et de leurs coûts et bénéfices
actions = [("Action-1", 20, 0.05), ("Action-2", 30, 0.1), ("Action-3", 50, 0.15),
           ("Action-4", 70, 0.2), ("Action-5", 60, 0.17), ("Action-6", 80, 0.25),
           ("Action-7", 22, 0.07), ("Action-8", 26, 0.11), ("Action-9", 48, 0.13),
           ("Action-10", 34, 0.27), ("Action-11", 42, 0.17), ("Action-12", 110, 0.09),
           ("Action-13", 38, 0.23), ("Action-14", 14, 0.01), ("Action-15", 18, 0.03),
           ("Action-16", 8, 0.08), ("Action-17", 4, 0.12), ("Action-18", 10, 0.14),
           ("Action-19", 24, 0.21), ("Action-20", 114, 0.18)]


def csv_to_list(csv_file):
    """
    Fonction copiant les données d'un fichier csv vers une liste, et efface les données
    erronées (inférieur ou égal à 0).
    """
    with open(csv_file) as dataset:
        dataset_read = csv.reader(dataset)

        dataset0 = []

        for row in dataset_read:
            dataset0.append(row)

    dataset0.pop(0)

    clean_dataset = []

    for row in dataset0:

        row[2] = int(round(float(row[1]) * (float(row[2]) / 100), 2) * 100)
        row[1] = int(float(row[1]) * 100)

        if row[1] > 0 and row[2] > 0:
            clean_dataset.append(row)

    return clean_dataset


def trouver_actions_optimales(actions, max_cout):
    num_actions = len(actions)
    # Remplissage des tableaux benefit et chosen_action en utilisant la programmation dynamique
    benefice = np.zeros((num_actions + 1, max_cout + 1))
    action_choisie = np.zeros((num_actions + 1, max_cout+1))

    for i in range(1, num_actions + 1):
        action = actions[i - 1]
        for j in range(1, max_cout + 1):
            if j < action[1]:
                # si l'action courante ne peut pas être achetée
                benefice[i][j] = benefice[i - 1][j]
                action_choisie[i][j] = -1
            else:
                # si l'action courante peut être achetée
                # comparaison du bénéfice de l'achat de l'action courante
                # avec le bénéfice de ne pas acheter l'action courante
                if benefice[i - 1][j] > benefice[i - 1][j - action[1]] + action[1] * action[2]:
                    benefice[i][j] = benefice[i - 1][j]
                    action_choisie[i][j] = -1
                else:
                    benefice[i][j] = benefice[i - 1][j - action[1]] + action[1] * action[2]
                    action_choisie[i][j] = i

    lst_actions_selectionnes = []
    while num_actions > 0 and max_cout > 0:
        if action_choisie[num_actions][max_cout] == -1:
            num_actions = num_actions - 1
        else:
            lst_actions_selectionnes.append(actions[int(action_choisie[num_actions][max_cout] - 1)])
            max_cout = max_cout - actions[int(action_choisie[num_actions][max_cout] - 1)][1]
            num_actions = num_actions - 1
    print(f"La rentabilité maximum obtenue est : ")
    print(f"{round(sum([num_actions[1] * num_actions[2] for num_actions in lst_actions_selectionnes]), 2)}")
    print(f"Le coût maximum est : {sum([num_actions[1] for num_actions in lst_actions_selectionnes])} euros, ")
    print(f"avec ces actions: {[num_actions[0] for num_actions in lst_actions_selectionnes]}")


def dynamic_compare_to_siena_data(infile_siena, csv_file):
    """
    Application des fonctions précédente sur les données de Sienna et on renvoie les résultats
    """
    list_siena = []

    for ligne in open(infile_siena):
        selection = ligne.find("Share")
        if selection == 0:
            action = slice(10)
            list_siena.append(ligne[action])

    print(list_siena)

    dataset = csv_to_list(csv_file)

    dataset_compare = []

    for i in dataset:
        for j in list_siena:
            if i[0] == j:
                dataset_compare.append(i)

    return trouver_actions_optimales(dataset_compare, 50000)


#trouver_actions_optimales(csv_to_list("dataset1_Python+P7.csv"), 5000)
#print(trouver_actions_optimales(csv_to_list('dataset2_Python+P7.csv'), 5000))

print(dynamic_compare_to_siena_data('solution1_Python+P7siena.txt', 'dataset1_Python+P7.csv'))
#print(dynamic_compare_to_siena_data('solution2_Python+P7siena.txt', 'dataset2_Python+P7.csv'))

