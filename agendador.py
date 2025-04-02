import matplotlib.pyplot as plt
import numpy as np

def fcfs(requests, start):
    return [start] + requests

def sstf(requests, start):
    sequence = [start]
    pending = requests[:]
    while pending:
        closest = min(pending, key=lambda x: abs(sequence[-1] - x))
        sequence.append(closest)
        pending.remove(closest)
    return sequence

def scan(requests, start, end=199):
    left = sorted([r for r in requests if r < start])
    right = sorted([r for r in requests if r >= start])
    return [start] + right + left[::-1]

def cscan(requests, start, end=199):
    right = sorted([r for r in requests if r >= start])
    left = sorted([r for r in requests if r < start])
    return [start] + right + [end, 0] + left

def calculate_movements(sequence):
    return sum(abs(sequence[i] - sequence[i-1]) for i in range(1, len(sequence)))

def plot_schedule(title, sequence):
    plt.figure(figsize=(8, 5))
    plt.plot(sequence, range(len(sequence)), marker='o', linestyle='-', color='b')
    plt.xlabel('Trilhas')
    plt.ylabel('Ordem de atendimento')
    plt.title(f"{title} - Movimentos: {calculate_movements(sequence)}")
    plt.grid()
    plt.show()

# Dados do problema
requests = [86, 147, 91, 177, 94, 150, 102, 175, 130]
start_position = 100

# Gerando sequências para cada algoritmo
fcfs_seq = fcfs(requests, start_position)
sstf_seq = sstf(requests, start_position)
scan_seq = scan(requests, start_position)
cscan_seq = cscan(requests, start_position)

# Gerando gráficos
plot_schedule("FCFS", fcfs_seq)
plot_schedule("SSTF", sstf_seq)
plot_schedule("SCAN", scan_seq)
plot_schedule("C-SCAN", cscan_seq)

# Exibir número de movimentos
print(f"Movimentos FCFS: {calculate_movements(fcfs_seq)}")
print(f"Movimentos SSTF: {calculate_movements(sstf_seq)}")
print(f"Movimentos SCAN: {calculate_movements(scan_seq)}")
print(f"Movimentos C-SCAN: {calculate_movements(cscan_seq)}")
