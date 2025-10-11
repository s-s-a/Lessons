
name = "Alex"
template = t"Hello {name!s:>10}!"
interpolation = template.interpolations[0]

print(interpolation.value)
print(interpolation.expression)
print(interpolation.conversion)
print(interpolation.format_spec)

