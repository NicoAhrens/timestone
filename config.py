from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config files
    parser.read(filename)

    # get section, default to postgresql
    # create a dict
    db = {}
    if parser.has_section(section):
        # parser.item gets every item under the section postgresql in the
        # database.ini in a tuple. and saves every tuple in a list
        params = parser.items(section)
        # print(params)
        # Iterating over the items in params list putting the first item of
        # every tuple into the dictionary db as a key. The corresponding values
        # are added from the second item of every tuple in the params list
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section{section} not found in {filename} file')

    return db


if __name__ == '__main__':
    config()
