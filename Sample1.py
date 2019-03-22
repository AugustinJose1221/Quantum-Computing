from qiskit import QuantumRegister ,ClassicalRegister ,QuantumCircuit
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_state_city
from qiskit.tools.visualization import plot_histogram
q = QuantumRegister(2 ,'q')
c = ClassicalRegister(2 ,'c')
qc = QuantumCircuit(q ,c)
Measure_Z = QuantumCircuit(q ,c)
Measure_Z.measure(q ,c)
qc.h(q[0])
qc.cx(q[0] ,q[1])
Measure_X = QuantumCircuit(q ,c)
Measure_X.measure(q ,c)
Result_Z = qc + Measure_Z
Result_X = qc + Measure_X
backend = BasicAer.get_backend("qasm_simulator")
job_Z = execute(Result_Z ,backend ,shots = 1000)
job_X = execute(Result_X ,backend ,shots = 1000)
R_Z = job_Z.result()
R_X = job_X.result()
count_Z = R_Z.get_counts(Result_Z)
count_X = R_X.get_counts(Result_X)
print(count_Z)
print(count_X)
plot_histogram(count_Z)
plot_histogram(count_X)
