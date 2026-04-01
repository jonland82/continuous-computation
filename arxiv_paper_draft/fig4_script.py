#!/usr/bin/env python3
"""Figure 4: Spectral amenability ratio for different signal types."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import erf

# ── Blue-gray professional palette ──────────────────────
DARK_STEEL  = '#1F3D6B'
MID_STEEL   = '#3A6EA8'
STEEL_LIGHT = '#7AAAC8'
DARK_GRAY   = '#3D3D3D'
MID_GRAY    = '#888888'

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'text.usetex': False,
    'axes.linewidth': 0.8,
    'figure.dpi': 300,
})

fig, ax = plt.subplots(1, 1, figsize=(5.0, 3.2))

tau = np.linspace(0.01, 3.0, 500)

# Pure tone
omega0   = 2.0
rho_tone = np.where(tau < np.pi / omega0, 1.0, 0.0)

# Narrowband: Gaussian spectrum
sigma_bw     = 0.3
W_tau        = 1.0 / (2 * tau)
f0           = omega0 / (2 * np.pi)
rho_narrowband = 0.5 * (erf((W_tau - f0) / (sigma_bw * np.sqrt(2))) +
                         erf((W_tau + f0) / (sigma_bw * np.sqrt(2))))
rho_narrowband = np.clip(rho_narrowband, 0, 1)

# Brownian-like: S(f) ~ 1/f^2
rho_brownian = (2 / np.pi) * np.arctan(W_tau)

# White noise
W_max      = 50.0
rho_white  = np.minimum(W_tau / W_max, 1.0)

# Lines: solid/dashed/dotted/dash-dot + shades for B&W readability
ax.plot(tau, rho_tone,      color=DARK_STEEL, lw=2.2, ls='-',
        label=r'pure tone $\sin(\omega_0 t)$')
ax.plot(tau, rho_narrowband, color=MID_STEEL,  lw=2.2, ls='--',
        label='narrowband signal')
ax.plot(tau, rho_brownian,  color=DARK_GRAY,  lw=2.0, ls=':',
        label=r'Brownian-like ($1/f^2$)')
ax.plot(tau, rho_white,     color=MID_GRAY,   lw=1.6, ls='-.',
        label='white noise')

ax.set_xlabel(r'Target dwell time $\tau$', fontsize=12)
ax.set_ylabel(r'Amenability ratio $\rho_{\mathcal{A}}(x, \tau)$', fontsize=12)
ax.set_xlim(0, 3.0)
ax.set_ylim(-0.05, 1.08)
ax.legend(fontsize=8, loc='center right', framealpha=0.92,
          edgecolor='#CCCCCC')

ax.annotate('all energy\npreserved', xy=(0.5, 1.0), xytext=(0.8, 0.72),
            fontsize=7, color=DARK_STEEL,
            arrowprops=dict(arrowstyle='->', color=DARK_STEEL, lw=0.7))

ax.annotate('energy lost to\nhigh-frequency tail', xy=(1.5, 0.2), xytext=(2.0, 0.5),
            fontsize=7, color=DARK_GRAY,
            arrowprops=dict(arrowstyle='->', color=DARK_GRAY, lw=0.7))

OUTDIR = r'c:\sandbox\sandbox\mutual_information_decay_physics\computation_amenable_conditions\arxiv_paper_draft\figures'
plt.savefig(OUTDIR + r'\fig4_spectral.pdf',
            bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Figure 4 saved.")
