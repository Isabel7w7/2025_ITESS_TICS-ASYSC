import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.fft import fft, fftfreq

# ---------------------------
# Ecuación del circuito RLC
# ---------------------------
def rlc(t, x, R, L, C, Vin):
    i, di = x
    d2i = (Vin(t) - R*di - i/C) / L
    return [di, d2i]

# ---------------------------
# Señales de entrada
# ---------------------------
def vin_seno(A, f, fase):
    return lambda t: A * np.sin(2*np.pi*f*t + fase)

# ---------------------------
# Simulación general
# ---------------------------
def simular(R, L, C, Vin, tmax=0.2, fs=20000):

    t = np.linspace(0, tmax, int(tmax*fs))

    sol = solve_ivp(
        rlc, [0, tmax], [0, 0],
        t_eval=t, args=(R, L, C, Vin)
    )
    i_t = sol.y[0]

    # FFT
    I_f = np.abs(fft(i_t))
    freqs = fftfreq(len(t), 1/fs)
    fase = np.angle(fft(i_t))

    # --------- 1) Corriente en el tiempo ----------
    plt.figure(figsize=(12,5))
    plt.plot(t, i_t)
    plt.title("Respuesta temporal i(t)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Corriente (A)")
    plt.grid()
    plt.show()

    # --------- 2) Magnitud FFT ----------
    plt.figure(figsize=(12,5))
    plt.plot(freqs[:len(freqs)//2], I_f[:len(freqs)//2])
    plt.title("Espectro de Magnitud |I(f)|")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid()
    plt.show()

    # --------- 3) Fase FFT ----------
    plt.figure(figsize=(12,5))
    plt.plot(freqs[:len(freqs)//2], fase[:len(freqs)//2])
    plt.title("Fase de la señal I(f) ")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Fase (rad)")
    plt.grid()
    plt.show()

    # --------- 4) Representación Polar ----------
    plt.figure(figsize=(8,8))
    ax = plt.subplot(111, projection='polar')
    ang = fase[:len(freqs)//2]
    mag = I_f[:len(freqs)//2]
    ax.plot(ang, mag)
    ax.set_title("Representación Polar de I(f)", va='bottom')
    ax.grid(True)
    plt.show()

    return t, i_t


# =======================================================
#            CASOS DE TAREA DE EXAMEN
# =======================================================

# Valores comerciales del Caso 1
R = 10          # ohmios
L = 1       # H
C = 100e-6       # F

# Señal del caso 1
entrada = vin_seno(
    A=8,        # Voltios A=V
    f=200,        # Hz
    fase=15       # rad
)

# Ejecutar simulación
t_res, i_res = simular(R, L, C, entrada)
