def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):

    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format("n_images", results_stats_dic["n_images"]))
    print("{:20}: {:3d}".format("n_dogs_img", results_stats_dic["n_dogs_img"]))
    print("{:20}: {:3d}".format("n_notdogs_img", results_stats_dic["n_notdogs_img"]))

    for key in results_stats_dic:
        if key.startswith("pct"):
            print("{:20}: {:5.1f}".format(key, results_stats_dic[key]))

    # Misclassified dogs (dog vs not-dog disagreement)
    if print_incorrect_dogs and (
        results_stats_dic["n_correct_dogs"] + results_stats_dic["n_correct_notdogs"]
        != results_stats_dic["n_images"]
    ):
        print("\nINCORRECT Dog/Not Dog Assignments:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Real: {:>26}  Classifier: {:>26}".format(
                    results_dic[key][0], results_dic[key][1]
                ))

    # Misclassified breeds (both say dog, but breed mismatch)
    if print_incorrect_breed and (
        results_stats_dic["n_correct_dogs"] != results_stats_dic["n_correct_breed"]
    ):
        print("\nINCORRECT Dog Breed Assignments:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Real: {:>26}  Classifier: {:>26}".format(
                    results_dic[key][0], results_dic[key][1]
                ))
