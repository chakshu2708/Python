test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))

res = dict(zip(test_keys,test_values))

print("Resultant dictionary is:" + str(res))