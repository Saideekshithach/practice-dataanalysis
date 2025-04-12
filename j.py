import json
x='{"name":"sai","age":22}'
z=json.loads(x)
print(z)
print(z["name"])
print(z["age"])
X={"name":"sai","age":22}
Y=json.dumps(X)
print(Y)
