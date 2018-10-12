from config.configuration import Configuration

def configuration(*argv):
    if argv is None:
        return Configuration.params
    data = Configuration.params
    for arg in argv:
        data = data[arg]
    return data