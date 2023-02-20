import pystache

def transform(template, table, mapping:dict={}):
    mappedTable = table if mapping == {} else [{mapping[key]: value for key, value in item.items()} for item in table]
    return [pystache.render(template, item) for item in mappedTable]
