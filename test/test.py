t = """COMPLETE PRODUCTION PLAN
SPLIT ORDER PO (8800942756, 8800942757, 8800942758)
(SO-BV-039941)[CTO]
Disti: (networld) PO: 4604155888
End Customer PO: 4604154236
watchpoint logistics
Nutanix MITF no PM Approval Required
NI002205132021 DD NTTD"""
print(t.encode())
my_str = "hello world"
my_str_as_bytes = str.encode(my_str)
type(my_str_as_bytes)  # ensure it is byte representation
my_decoded_str = my_str_as_bytes.decode()
type(my_decoded_str)  # ensure it is string representation

print(id(...))

print(id(...))


print(divmod(10, 3))