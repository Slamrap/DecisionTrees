from math import log
from Tree import *

frequency = {}

def helps(table, examples, attributes, target_attribute):
    for attribute in attributes[0:-1]:
        print("gain(" + attribute + ", " + target_attribute + ") = " + str(gain(examples, attributes, attribute, target_attribute)))

def id3(table, examples, attributes, target_attribute):
    """

    :param table:
    :param examples:
    :param attributes:
    :param target_attribute:
    :return:
    """

    target_index = attributes.index(target_attribute)
    values = [row[target_index] for row in examples]
    #values = table[target_attribute].values.tolist()
    if not examples or (len(attributes) - 2) <= 0:  # no more attributes to analize
        return most_common_value(examples, attributes, target_attribute)
    elif values.count(values[0]) == len(values): # all examples are positive or negative
        return values[0]
    else:
        best_attribute = get_best_attribute(examples, attributes, target_attribute)
        print("Best:" + best_attribute)
        #print(best_attribute)
        tree = {best_attribute : {}}

        uniques = get_uniques(get_column(examples, attributes.index(best_attribute)))
        for value in uniques:
            #new_examples = table[table[best_attribute] == value].values.tolist()
            new_examples = get_examples(examples, attributes, best_attribute, value)

            #table.drop(best_attribute, axis=1, inplace=True)  # remove best atribute from dataset
            # new_attributes = table.columns.tolist()
            new_attributes = attributes[:]
            new_attributes.remove(best_attribute)
            #new_examples = delete_col(new_examples, attributes.index(best_attribute))

            #print(table.shape)
            new_node = id3(table, new_examples, new_attributes, target_attribute)

            tree[best_attribute][value] = new_node

        return tree


def ID32(examples, attributes, target_attribute):
    target_index = attributes.index(target_attribute)
    values = [row[target_index] for row in examples]

    if not examples or (len(attributes) - 2) <= 0:        # no more attributes to analise
        return most_common_value(examples, attributes, target_attribute)
    elif values.count(values[0]) == len(values):          # all examples are positive or negative
        return values[0]
    else:
        best_attribute = get_best_attribute(examples, attributes, target_attribute)

        node = Tree(best_attribute)
        #tree = {best_attribute: {}}

        uniques = get_uniques(get_column(examples, attributes.index(best_attribute)))
        for value in uniques:
            new_node = Tree(value)
            new_examples = get_examples(examples, attributes, best_attribute, value)

            new_attributes = attributes[:]
            new_attributes.remove(best_attribute)

            branch = ID32(new_examples, new_attributes, target_attribute)

            new_node.branch.append(branch)
            node.branch.append(new_node)

            #node.branch.append(new_node)
            #node[best_attribute][value] = new_node

        return node


def entropy(examples, attributes, target_attribute):
    """
    Calculates the entropy for the target_attribute, using the given examples
    :param examples: list of examples (list of lists)
    :param attributes: list of attributes
    :param target_attribute: string of the target_attribute name
    :return: returns the obtained entropy
    """

    ent = 0
    probs = probability(examples, attributes, target_attribute)
    for p in probs.values():
        ent += - p * log(p, 2)
    return ent


def gain(examples, attributes, cur_attr, target_attribute):
    """
    Calculates the information gain
    :param examples: list of examples (list of lists)
    :param attributes: list of attributes
    :param target_attribute: string of the target_attribute name
    :return: returns the information gain
    """

    target_index = attributes.index(cur_attr)
    probs = probability(examples, attributes, cur_attr)

    sub_gain = 0.0
    for key, prob in probs.items():
        sub_examples = [value for value in examples if value[target_index] == key]
        sub_gain += prob * entropy(sub_examples, attributes, target_attribute)

    info_gain = entropy(examples, attributes, target_attribute) - sub_gain
    return info_gain


def probability(examples, attributes, target_attribute):
    """
    Calculates de probability of each unique value from the target_attribute column
    :param examples: list of examples (list of lists)
    :param attributes: list of attributes
    :param target_attribute: string of the target_attribute name
    :return: return a dictionary where the key is each unique value from the target_attribute column
    and the value is the probability
    """
    target_index = attributes.index(target_attribute)
    elems = []
    for val in examples:
        elems.append(val[target_index])
    values = list(set(elems))

    p = {}
    for c in values:
        p[c] = elems.count(c) / len(elems)
    return p


def get_best_attribute(examples, attributes, target_attribute):
    """

    :param table:
    :param examples:
    :param attributes:
    :param target_attribute:
    :return:
    """

    best_gain = float("-inf")
    for attribute in attributes:
        gain_info = gain(examples, attributes, attribute, target_attribute)
        print("gain(" + target_attribute + ", " + attribute + ") = " + str(gain_info))
        if gain_info > best_gain and attribute != target_attribute:
            best_gain = gain_info
            best_attribute = attribute
    return best_attribute


def most_common_value(examples, attributes, target_attribute):
    """

    :param examples:
    :param attributes:
    :param target_attribute:
    :return:
    """

    target_index = attributes.index(target_attribute)
    elems = []
    for val in examples:
        elems.append(val[target_index])
    values = list(set(elems))

    max_count = 0
    most_common_val = ""
    for c in values:
        if elems.count(c) > max_count:
            max_count = elems.count(c)
            most_common_val = c
    return most_common_val


def print_tree(table, tree, level):
    attributes = table.columns.tolist()

    for key, val in tree.items():
        if isinstance(val, dict):  # if is a node
            if key in attributes:
                print("\t" * level, "<" + key + ">:")
            else:
                print("\t" * level, key + ":")
            print_tree(table, val, level + 1)
        else:
            print("-------" + key + ", " + val)
            all_vals = table[key].values.tolist()
            count_val = all_vals.count(val)
            print("\t" * level, key + ":" + "(" + count_val + ")")


def print_tree2(values, attributes, tree, level=0, parent=None, label=""):
    if not tree or len(tree) == 0:
        print("\t" * level, "-")
    else:
        for key, value in tree.items():
            if isinstance(value, dict):
                if key in attributes:
                    print("\t" * level, "<" + key + ">:")
                    count_value(values, attributes, key)
                else:
                    print("\t" * level, key + ":")
                    label = key
                    key = parent
                print_tree2(values, attributes, value, level+1, key, label)
            else:
                print("\t" * level, key + ":", value, "(" + str(frequency[(parent, key, value)]) + ")")




def count_value(values, attributes, key):
    attr_index = attributes.index(key)
    for val in values:
        if (key, val[attr_index], val[-1]) in frequency:
            frequency[(key, val[attr_index], val[-1])] += 1
        else:
            frequency[(key, val[attr_index], val[-1])] = 1

def delete_col(examples, index):
    for ex in examples:
        del ex[index]
    return examples

def get_examples(examples, attributes, best_attribute, target):
    new_examples = []
    best_index = attributes.index(best_attribute)
    for ex in examples:
        if ex[best_index] == target:
            new_row = []
            for i in range(len(ex)):
                if i!= best_index:
                    new_row.append(ex[i])
            new_examples.append(new_row)
    return new_examples

def get_column(examples, index):
    res = []
    for ex in examples:
        res.append(ex[index])
    return res

def get_uniques(examples):
    return list(set(examples))