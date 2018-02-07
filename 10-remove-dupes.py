def dedupe_list(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
unduped = list(dedupe_list(a))
print(unduped)

def dedupe_dict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe_dict(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe_dict(a, key=lambda d: d['x'])))

# you can do set(a) but it won't preserve ordering