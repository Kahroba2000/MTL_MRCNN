def split_data(json_edited):
    import os
    import configparser
    import json
    import random
    import copy

    print("[INFO] Splitting dataset")

    # creating directory if it does not exist
    os.makedirs("./datasets", exist_ok=True)

    config = configparser.ConfigParser()
    config.read('config_default.ini')

    train_split = float(config.get('DATA_SPLITTER_SETTINGS', 'train_split'))
    validation_split = float(config.get('DATA_SPLITTER_SETTINGS', 'validation_split'))
    test_split = float(config.get('DATA_SPLITTER_SETTINGS', 'test_split'))

    assert train_split + validation_split + test_split == 1.0, "Dataset split values must sum to 1"

    dataset_skeleton = copy.deepcopy(json_edited)
    dataset = copy.deepcopy(json_edited)

    dataset_skeleton.pop('annotations', None)

    # this writing to file is for debugging help only not necessary
    # with open('temp.json', 'w') as json_file:
    #     json.dump(dataset_skeleton, json_file)

    # because in python setting a variable sets a reference to the variable it is necessary to use this syntax
    # to create new lists
    dataset_train = copy.deepcopy(dataset_skeleton)
    dataset_validation = copy.deepcopy(dataset_skeleton)
    dataset_test = copy.deepcopy(dataset_skeleton)

    dataset_length = len(dataset['annotations'])

    # shuffling the dataset to prevent sets containing annotations of a single label
    temp_list = list(dataset['annotations'])
    random.shuffle(temp_list)

    train_number = int(dataset_length * train_split)
    validation_number = int(dataset_length * validation_split)
    test_number = int(dataset_length * test_split)

    # This won't create perfect ratios as defined in the settings file, but it doesn't matter
    train_list = temp_list[:train_number]
    validation_list = temp_list[train_number:train_number + validation_number]
    test_list = temp_list[train_number + validation_number:]

    # each dataset is a dictionary, contains annotations which is a list, which contains dictionaries

    annotations_list = []
    for index, i in enumerate(train_list):
        # print(i)
        annotations_list.append(i)
    dataset_train.update({'annotations': annotations_list})

    annotations_list = []
    for index, i in enumerate(validation_list):
        # print(i)
        annotations_list.append(i)
    dataset_validation.update({'annotations': annotations_list})

    annotations_list = []
    for index, i in enumerate(test_list):
        # print(i)
        annotations_list.append(i)
    dataset_test.update({'annotations': annotations_list})

    with open("./datasets/train.json", 'w') as json_file:
        json.dump(dataset_train, json_file)
    with open("./datasets/validation.json", 'w') as json_file:
        json.dump(dataset_validation, json_file)
    with open("./datasets/test.json", 'w') as json_file:
        json.dump(dataset_test, json_file)

    print("[INFO] Dataset splitting completed")
