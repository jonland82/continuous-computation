#!/usr/bin/env python3
"""Figure 3: The partition of trajectory space into A (amenable) and N (non-amenable)."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# ── Blue-gray professional palette ──────────────────────
DARK_STEEL  = '#1F3D6B'
MID_STEEL   = '#3A6EA8'
DARK_GRAY   = '#3D3D3D'
MID_GRAY    = '#6B6B6B'
ACCENT_WARM = '#5A5040'
BLUE_BG     = '#DCE9F5'
GRAY_BG     = '#EBEBEB'

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'text.usetex': False,
    'axes.linewidth': 0.8,
    'figure.dpi': 300,
})

fig, ax = plt.subplots(1, 1, figsize=(6.0, 4.2))
ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-3.8, 3.8)
ax.set_aspect('equal')
ax.axis('off')

# ── Outer region: N ────────────────────────────────────────
outer = plt.Rectangle((-5.2, -3.5), 10.4, 7.0,
                       fc=GRAY_BG, ec='none', alpha=0.5, zorder=0)
outer.set_clip_on(False)
ax.add_patch(outer)
ax.plot([-5.2, 5.2, 5.2, -5.2, -5.2], [-3.5, -3.5, 3.5, 3.5, -3.5],
        color='#BBBBBB', lw=0.8, zorder=0)

ax.text(-4.2, 3.05, r'$\mathcal{N}$', fontsize=18, color=DARK_GRAY, fontweight='bold')
ax.text(-4.5, 2.4, 'non-amenable\n$\\mu_W(\\mathcal{N}) = 1$', fontsize=8, color=MID_GRAY,
        ha='left', va='top')

# ── Inner region: A ────────────────────────────────────────
ell_main = Ellipse((0, 0), 6.4, 4.4,
                   fc=BLUE_BG, ec=ACCENT_WARM, lw=2.0, alpha=0.7, zorder=1)
ax.add_patch(ell_main)
ax.text(0,    1.7,  r'$\mathcal{A}$', fontsize=18, color=DARK_STEEL,
        fontweight='bold', ha='center')
ax.text(0,    1.15, r'$\mu_W(\mathcal{A}) = 0$', fontsize=8, color=MID_GRAY, ha='center')

# ── Stratification rings ────────────────────────────────────
for r_scale in [0.75, 0.5]:
    ell = Ellipse((0, 0), 6.4*r_scale, 4.4*r_scale,
                  fc='none', ec=MID_STEEL, ls='--', lw=0.9, alpha=0.7, zorder=2)
    ax.add_patch(ell)

ax.annotate(r'$\tau_{\min}$ increasing $\rightarrow$', xy=(-0.5, -1.65), xytext=(2.5, -2.4),
            fontsize=8, color=MID_STEEL,
            arrowprops=dict(arrowstyle='->', color=MID_STEEL, lw=0.8))

# ── Boundary label ──────────────────────────────────────────
ax.text(3.55, 0.3, '$\\partial\\mathcal{A}$: spectral\ngap closes',
        fontsize=8, color=ACCENT_WARM, ha='left')

# ── Examples in N ──────────────────────────────────────────
examples_N = [
    (-3.7, -1.0, '$\\sin(1/t)$'),
    ( 4.0, -1.5, 'Brownian'),
    (-3.7, -2.1, 'thermal noise'),
]
for (x, y, label) in examples_N:
    ax.text(x, y, label, fontsize=8, color=DARK_GRAY,
            bbox=dict(boxstyle='round,pad=0.3', fc='#D8D8D8', ec='#AAAAAA',
                      alpha=0.85, lw=0.7),
            ha='center', va='center')

# ── Examples in A ──────────────────────────────────────────
examples_A = [
    ( 0.0,  0.0, 'transistor'),
    (-1.5, -0.5, '$\\sin(t)$'),
    ( 1.5, -0.5, 'double-well'),
    ( 0.0,  0.7, 'neural spike'),
]
for (x, y, label) in examples_A:
    ax.text(x, y, label, fontsize=8, color=DARK_STEEL,
            bbox=dict(boxstyle='round,pad=0.3', fc='#B8D0E8', ec='#7AAAC8',
                      alpha=0.85, lw=0.7),
            ha='center', va='center')

# ── Dissipation arrow ───────────────────────────────────────
ax.annotate('', xy=(0.0, -1.0), xytext=(-3.7, -1.6),
            arrowprops=dict(arrowstyle='->', color=MID_STEEL, lw=2.0, ls='--'))
ax.text(-2.0, -1.7, '$\\sigma > \\sigma_c$', fontsize=9, color=MID_STEEL, ha='center')

# ── Properties box ──────────────────────────────────────────
props_text = ('$\\mathcal{A}$ is not a subspace\n'
              '$\\mathcal{A}$ is not convex\n'
              '$\\mathcal{A}$ is not closed\n'
              'Stratified by $\\tau_{\\min}$')
ax.text(-5.0, -2.7, props_text, fontsize=7, color=MID_GRAY,
        family='monospace', va='top',
        bbox=dict(boxstyle='round,pad=0.4', fc='white', ec='#CCCCCC', alpha=0.85))

OUTDIR = r'c:\sandbox\sandbox\mutual_information_decay_physics\computation_amenable_conditions\arxiv_paper_draft\figures'
plt.savefig(OUTDIR + r'\fig3_geometry.pdf',
            bbox_inches='tight', pad_inches=0.15)
plt.close()
print("Figure 3 saved.")
