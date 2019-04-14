from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit import BasicAer
n1 = input("Enter a binary number with less than 8 digits:")
n2 = input("Enter another binary number with less than 8 digits:")

l1 = len(n1)
l2 = len(n2)
n = 0

if l1>l2:
    n = l1
else:
    n = l2

a = QuantumRegister(n)      #First number
b = QuantumRegister(n+1)    #Second number
c = QuantumRegister(n)      #Carry bits

cl = ClassicalRegister(n+1)

qc = QuantumCircuit(a,b,c,cl)

for i in range(l1):
    if n1[i] == "1":
        qc.x(a[l1-(i+1)])
for i in range(l2):
    if n2[i] == "1":
        qc.x(b[l2-(i+1)])

for i in range(n-1):
    qc.ccx(a[i],b[i],c[i+1])
    qc.cx(a[i],b[i])
    qc.ccx(c[i],b[i],c[i+1])

qc.ccx(a[n-1],b[n-1],b[n])
qc.cx(a[n-1],b[n-1])
qc.ccx(c[n-1],b[n-1],b[n])

qc.cx(c[n-1],b[n-1])
for i in range(n-1):
    qc.ccx(c[(n-2)-i],b[(n-2)-i],c[(n-1)-i])
    qc.cx(a[(n-2)-i],b[(n-2)-i])
    qc.ccx(a[(n-2)-i],b[(n-2)-i],c[(n-1)-i])

    qc.cx(c[(n-2)-i],b[(n-2)-i])
    qc.cx(a[(n-2)-i],b[(n-2)-i])

for i in range(n+1):
    qc.measure(b[i],cl[i])
print(qc)

backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=2)
counts = job.result().get_counts(qc)
print(counts)
