#!/usr/bin/env python3
"""Figure 2: Dissipation-lumpability inequality and thermodynamic computation epochs."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Blue-gray professional palette ──────────────────────
DARK_STEEL  = '#1F3D6B'
MID_STEEL   = '#3A6EA8'
DARK_GRAY   = '#3D3D3D'
MID_GRAY    = '#6B6B6B'
ACCENT_WARM = '#5A5040'
BLUE_BG     = '#DCE9F5'
GRAY_BG     = '#EBEBEB'
WARN_BG     = '#E8E4DC'   # warm light gray (subcritical region)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'text.usetex': False,
    'axes.linewidth': 0.8,
    'figure.dpi': 300,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.2),
                                gridspec_kw={'wspace': 0.42})

# ── Panel A: lambda vs sigma ──────────────────────────────
sigma  = np.linspace(0, 2.2, 500)
lam_eq = 1.0
c_val  = 1.0
sigma_c = (lam_eq / c_val)**2

lam = np.maximum(0, lam_eq - c_val * np.sqrt(sigma))

ax1.fill_between(sigma, 0, lam,  color=GRAY_BG,  alpha=0.7,
                 label=r'$\lambda > 0$: imperfect lumpability')
ax1.fill_between(sigma[sigma >= sigma_c], 0, 0.02, color=BLUE_BG, alpha=0.8)
ax1.axhline(0, color=MID_GRAY, lw=0.5)

ax1.plot(sigma, lam, color=DARK_STEEL, lw=2.5, zorder=3)

# Critical point — open circle for contrast
ax1.plot(sigma_c, 0, 'o', color=DARK_GRAY, markersize=8,
         markerfacecolor='white', markeredgewidth=1.8, zorder=4)
ax1.annotate('critical point\n$\\sigma_c$', xy=(sigma_c, 0), xytext=(1.5, 0.35),
             fontsize=8, color=DARK_GRAY, ha='center',
             arrowprops=dict(arrowstyle='->', color=DARK_GRAY, lw=0.8))

ax1.annotate('dissipation\nreduces $\\lambda$',
             xy=(0.82, 0.12), xytext=(1.35, 0.68),
             fontsize=8, color=MID_STEEL, ha='center',
             arrowprops=dict(arrowstyle='->', color=MID_STEEL, lw=1.6))

ax1.set_xlabel('Entropy production $\\sigma$', fontsize=11)
ax1.set_ylabel('Lumpability error $\\lambda$', fontsize=11)
ax1.set_xlim(-0.05, 2.2)
ax1.set_ylim(-0.08, 1.1)
ax1.set_xticks([0, sigma_c])
ax1.set_xticklabels(['$0$', '$\\sigma_c$'])
ax1.set_yticks([0, lam_eq])
ax1.set_yticklabels(['$0$', '$\\lambda_{\\mathrm{eq}}$'])
ax1.set_title('(a) Dissipation\u2013lumpability', fontsize=11, fontweight='bold')

# ── Panel B: Epoch vs power ────────────────────────────────
W_dot = np.linspace(0.01, 2.0, 500)
W_c   = 1.0
theta = 0.5
Delta = 0.1

lam_W  = np.maximum(0, 1.0 - np.sqrt(W_dot / W_c))
p_eps  = 0.01
epoch  = np.where(lam_W + 2*p_eps > 0.001,
                  theta * Delta / (lam_W + 2*p_eps),
                  theta * Delta / 0.001)
epoch  = np.minimum(epoch, 30)

ax2.fill_betweenx([0, 32], 0,   W_c, color=WARN_BG, alpha=0.6)
ax2.fill_betweenx([0, 32], W_c, 2.0, color=BLUE_BG, alpha=0.5)
ax2.axvline(W_c, color=ACCENT_WARM, ls='--', lw=0.9)

ax2.plot(W_dot, epoch, color=DARK_STEEL, lw=2.5, zorder=3)

ax2.text(0.4,  25, 'subcritical',  fontsize=8, color=MID_GRAY, ha='center')
ax2.text(1.5,  25, 'supercritical', fontsize=8, color=MID_GRAY, ha='center')

ax2.set_xlabel('Power budget $\\dot{W}$', fontsize=11)
ax2.set_ylabel('Computation epoch $T_{\\mathrm{comp}}$', fontsize=11)
ax2.set_xlim(-0.02, 2.0)
ax2.set_ylim(0, 32)
ax2.set_xticks([0, W_c, 2.0])
ax2.set_xticklabels(['$0$', '$\\dot{W}_c$', '$2$'], color=DARK_GRAY)
ax2.get_xticklabels()[1].set_color(ACCENT_WARM)
ax2.set_title('(b) Power\u2013duration trade-off', fontsize=11, fontweight='bold')

OUTDIR = r'c:\sandbox\sandbox\mutual_information_decay_physics\computation_amenable_conditions\arxiv_paper_draft\figures'
plt.savefig(OUTDIR + r'\fig2_dissipation.pdf',
            bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Figure 2 saved.")
