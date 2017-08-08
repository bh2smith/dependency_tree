
def beautify(d, offset=0):
    """
    :param d: dict
    :param offset: int
    :return: str

    d is a nested dictionary representing a dependency tree, offset for
    indentation of lower level dependencies. Returns a python string
    for visualization of the dependency tree.

    Example:
    > beautify({'base': None, 'web_kanban': {'web': {'base': None}}})
    yields;
    |base
    |web_kanban
    |----web
    |--------base
    """
    if not d:
        return ''
    res = ''
    for k in sorted(d.keys()):
        res += '\n|' + '-' * offset + k
        if d[k]:
            res += beautify(d[k], offset + 4)

    return res


def depth(d, level=0):
    """
    :param d: dict
    :param level: int
    :return: int

    returns depth of a nested dictionary
    """
    if not d:
        return level
    return max(depth(d[k], level + 1) for k in d)


def keywords(d):
    """
    :param d: dict
    :return: list
    Transforms nested dictionary into list of distinct keys.
    """
    if not d:
        return []
    res = d.keys()
    for v in d.values():
        if v:
            res += keywords(v)
    return list(set(res))
