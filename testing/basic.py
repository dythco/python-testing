def parser(
    data,
    delimiter = ',',
    transform = None
):
    parts = data.split(delimiter)

    if transform is None:
        return parts

    return [transform(x) for x in parts]