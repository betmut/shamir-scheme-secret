from importlib.metadata import distributions

print(", ".join(
    f"{dist.metadata['Name']} {dist.version}"
    for dist in distributions()
))
