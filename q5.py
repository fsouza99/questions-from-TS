def reverse_str(mystr):
	"""Reverses a string."""
	buffer = [mystr[i] for i in range(len(mystr) - 1, -1, -1)]
	return ''.join(buffer)

target = 'Teste de Reversão de String'
print(reverse_str(target))