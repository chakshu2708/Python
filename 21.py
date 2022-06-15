def capitalize_first_letter(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
 
print(capitalize_first_letter('javaScript'))
print(capitalize_first_letter('python', True))
