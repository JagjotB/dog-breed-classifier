def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = dict()

    # Read dog names from file into dictionary
    with open(dogfile, "r") as f:
        for line in f:
            dog_name = line.rstrip().lower()
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print("** Warning: Duplicate dog name found:", dog_name)

    # Add is-a-dog flags to results_dic
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Pet label is-a-dog?
        pet_is_dog = 1 if pet_label in dognames_dic else 0

        # Classifier label is-a-dog? (can be multiple comma-separated names)
        classifier_is_dog = 0
        for name in classifier_label.split(","):
            if name.strip() in dognames_dic:
                classifier_is_dog = 1
                break

        results_dic[key].extend([pet_is_dog, classifier_is_dog])
