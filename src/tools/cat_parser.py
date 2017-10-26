"""
A parser for the catagories provided by the uc berkeley enron email dump

for more info see:
http://bailando.sims.berkeley.edu/enron_email.html

category definitions provided at ../enron_categories
"""


def parse_line(line):
    split_line = line.split(',')
    return map(int, split_line)


def parse_categories(file_like):
    """

    :param file_like: file_like object (with the readlines method) that contains the category information for an email
    :return: dictionary of categories of the form {category_class: [categories]}. Note that a single email can belong
      to many (or none) categories of a given class
    """
    categories = {cat: [] for cat in (1, 2, 3, 4)}
    for line in file_like.readlines():
        parsed = parse_line(line)
        categories[parsed[0]].append(parsed[1])

    return categories


def parse_file(file_path):
    return parse_categories(open(file_path, 'r'))
