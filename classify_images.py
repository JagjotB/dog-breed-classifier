from classifier import classifier

def classify_images(images_dir, results_dic, model):

    for key in results_dic:
        image_path = images_dir + key

        classifier_label = classifier(image_path, model)
        classifier_label = classifier_label.lower().strip()

        pet_label = results_dic[key][0]

        if pet_label in classifier_label:
            match = 1
        else:
            match = 0

        results_dic[key].extend([classifier_label, match])
