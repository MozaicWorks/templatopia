import pystache


def transform(template, values, mapping:dict={}):
    mappedValues = values if mapping == {} else {mapping.get(key, key): value for key, value in values.items()}
    return pystache.render(template, mappedValues)
