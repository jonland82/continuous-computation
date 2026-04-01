#!/usr/bin/env python3
"""Figure 1: Two trajectories with identical range but different amenability."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Blue-gray professional palette ──────────────────────
DARK_STEEL   = '#1F3D6B'   # dark steel blue  (amenable / primary)
MID_STEEL    = '#3A6EA8'   # medium steel blue (samples)
DARK_GRAY    = '#3D3D3D'   # dark gray         (non-amenable)
MID_GRAY     = '#6B6B6B'   # medium gray       (annotations, gridlines)
ACCENT_WARM  = '#5A5040'   # warm dark gray    (crossing markers)
BLUE_BG      = '#DCE9F5'   # light blue-gray   (R region)
GRAY_BG      = '#EBEBEB'   # light gray        (L region)
STRIP_A      = '#3A6EA8'   # symbol strip amenable
STRIP_N      = '#9AABB8'   # symbol strip non-amenable

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'text.usetex': False,
    'axes.linewidth': 0.8,
    'figure.dpi': 300,
})

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.5, 5.0),
                                gridspec_kw={'hspace': 0.48})

# ── Panel A: sin(t) ──────────────────────────────────────
t1 = np.linspace(0.01, 6.8, 2000)
y1 = np.sin(t1)

ax1.axhspan(0,     1.15, color=BLUE_BG, alpha=0.6, zorder=0)
ax1.axhspan(-1.15, 0,    color=GRAY_BG, alpha=0.6, zorder=0)
ax1.axhline(0, color=MID_GRAY, ls='--', lw=0.6, zorder=1)

ax1.plot(t1, y1, color=DARK_STEEL, lw=2.0, zorder=3)

for zc in [np.pi, 2*np.pi]:
    ax1.axvline(zc, color=ACCENT_WARM, ls='--', lw=0.9, alpha=0.8, zorder=2)

Delta = 0.8
samples_t = np.arange(0, 6.8, Delta)
samples_y = np.sin(samples_t)
ax1.scatter(samples_t, samples_y, color=MID_STEEL, s=20, zorder=4,
            edgecolors='white', linewidths=0.5)

# Symbol strip — two shades distinguish R vs L
for i in range(len(samples_t) - 1):
    c = STRIP_A if samples_y[i] >= 0 else STRIP_N
    ax1.fill_between([samples_t[i], samples_t[i+1]], -1.35, -1.2, color=c, alpha=0.85)

ax1.set_xlim(-0.2, 7.0)
ax1.set_ylim(-1.45, 1.15)
ax1.set_ylabel('$x(t)$', fontsize=12)
ax1.set_title(r'$x(t) = \sin(t)$  —  $\mathbf{Amenable}$',
              fontsize=12, fontweight='bold', color=DARK_STEEL)

ax1.text(5.8,  0.85, '$R$', fontsize=11, color=DARK_STEEL, fontweight='bold')
ax1.text(5.8, -0.95, '$L$', fontsize=11, color=DARK_GRAY,  fontweight='bold')
phase_label_box = dict(boxstyle='round,pad=0.12', facecolor='white', edgecolor='none', alpha=0.85)
ax1.text(np.pi + 0.18,  -0.95, r'$\pi$',   fontsize=10, ha='center', va='center',
         color=ACCENT_WARM, bbox=phase_label_box)
ax1.text(2*np.pi + 0.18, -0.95, r'$2\pi$', fontsize=10, ha='center', va='center',
         color=ACCENT_WARM, bbox=phase_label_box)

# "uniform spacing" — placed in clear R-region upper right, arrow down to a sample dot
ax1.annotate('uniform spacing', xy=(4.8, -0.998), xytext=(5.2, 0.52),
             fontsize=10, color=ACCENT_WARM, ha='center',
             arrowprops=dict(arrowstyle='->', color=ACCENT_WARM, lw=0.9))

# ── Panel B: sin(1/t) ────────────────────────────────────
t2a = np.linspace(0.035, 1.0, 8000)
t2b = np.linspace(1.0,   6.8, 2000)
y2a = np.sin(1.0 / t2a)
y2b = np.sin(1.0 / t2b)

ax2.axhspan(0,     1.15, color=BLUE_BG, alpha=0.6, zorder=0)
ax2.axhspan(-1.15, 0,    color=GRAY_BG, alpha=0.6, zorder=0)
ax2.axhline(0, color=MID_GRAY, ls='--', lw=0.6, zorder=1)

ax2.plot(t2a, y2a, color=DARK_GRAY, lw=1.5, zorder=3)
ax2.plot(t2b, y2b, color=DARK_GRAY, lw=1.5, zorder=3)

# Bracket showing accumulation
ax2.annotate('', xy=(0.035, -1.35), xytext=(0.7, -1.35),
             arrowprops=dict(arrowstyle='-', color=DARK_GRAY, lw=1.2))
ax2.plot([0.035, 0.035], [-1.4, -1.3], color=DARK_GRAY, lw=1.2)
ax2.plot([0.7,   0.7  ], [-1.4, -1.3], color=DARK_GRAY, lw=1.2)
ax2.text(0.48, -1.60, r'$\infty$ crossings', fontsize=11, ha='center', color=DARK_GRAY)

ax2.set_xlim(-0.2, 7.0)
ax2.set_ylim(-1.75, 1.15)
ax2.set_xlabel('$t$', fontsize=12)
ax2.set_ylabel('$x(t)$', fontsize=12)
ax2.set_title(r'$x(t) = \sin(1/t)$  —  $\mathbf{Non\text{-}amenable}$  [x]',
              fontsize=12, fontweight='bold', color=DARK_GRAY)

ax2.text(5.8,  0.85, '$R$', fontsize=11, color=DARK_STEEL, fontweight='bold')
ax2.text(5.8, -0.95, '$L$', fontsize=11, color=DARK_GRAY,  fontweight='bold')

# Point at the dense oscillation region; text placed far right in clear R space
ax2.annotate('crossings accumulate\nat $t=0$', xy=(0.1, -0.75), xytext=(1.8, -0.62),
             fontsize=10, color=DARK_GRAY, ha='center',
             arrowprops=dict(arrowstyle='->', color=DARK_GRAY, lw=0.9))

OUTDIR = r'c:\sandbox\sandbox\mutual_information_decay_physics\computation_amenable_conditions\arxiv_paper_draft\figures'
plt.savefig(OUTDIR + r'\fig1_two_trajectories.pdf',
            bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Figure 1 saved.")
