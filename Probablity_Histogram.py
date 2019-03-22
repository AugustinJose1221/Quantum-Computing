import numpy as np
from qiskit import QuantumCircuit ,ClassicalRegister ,QuantumRegister
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_state_city
from qiskit.tools.visualization import plot_histogram
from qiskit import IBMQ
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor


q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
circ = QuantumCircuit(q)
meas = QuantumCircuit(q, c)
meas.barrier(q)

circ.h(q[0])
circ.cx(q[0], q[1])
circ.cx(q[0], q[2])

meas.measure(q,c)
qc = circ+meas
qc.draw(output='mpl')

backend_sim = BasicAer.get_backend('qasm_simulator')
job_sim = execute(qc, backend_sim, shots=1024)
result_sim = job_sim.result()
counts = result_sim.get_counts(qc)
print(counts)
plot_histogram(counts)


IBMQ.load_accounts()
print("Available backends")
IBMQ.backends()

large_enough_devices = IBMQ.backends(filters=lambda x : x.configuration().n_qubits >3 and not x.configuration().simulator)
backend = least_busy(large_enough_devices)
print("The best backend is "+ backend.name())

shots = 1024
max_credits = 3
job_exp = execute(qc, backend=backend, shots=shots, max_credits=max_credits)
job_monitor(job_exp)
result_exp = job_exp.result()

counts_exp = result_exp.get_counts(qc)
plot_histogram([counts_exp,counts])
