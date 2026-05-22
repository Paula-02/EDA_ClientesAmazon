import numpy as np

# ── Paleta colores global ────────────────────────────────────────────────────────────
COLORES = ["#0072B2","#E69F00","#009E73","#D55E00",
           "#CC79A7","#56B4E9","#F0E442","#333333"]

COLORES_SEG = {
    "Comprador activo":  "#0072B2",
    "Navegador pasivo":  "#E69F00",
    "Comprador directo": "#009E73",
    "Usuario ocasional": "#999999",
}

COLORES_H1 = ["#eff3ff", "#bdd7e7", "#6baed6", "#3182bd", "#08519c", "#081d58"]

COLORES_H2 = ["#edf8fb", "#b2e2e2", "#66c2a4", "#238b45"]

COLORES_H3=["#d8b365", "#f5f5f5", "#5ab4ac"]

COLORES_H4 = ["#a6611a","#dfc27d","#f5f5f5","#80cdc1", "#018571"]

COLORES_Q1 = ["#D55E00","#E69F00","#F0E442","#56B4E9","#0072B2"]

# ── Significancia ─────────────────────────────────────────────────────────────
def significancia(p):
    if p < 0.001: return "Altamente significativo"
    if p < 0.01:  return "Significativo"
    if p < 0.05:  return "Sutilmente significativo"
    return "No Significativo"

# ── Anotaciones ──────────────────────────────────────────────────────────────
def anotar_barras(ax, bars, valores=None, fmt="{:.1f}", offset_x=0, offset_y=2,
                  horizontal=False, fontsize=9):

    for bar, val in zip(bars, valores if valores is not None else [b.get_width() if horizontal else b.get_height() for b in bars]):
        if horizontal:
            ax.text(bar.get_width() + offset_x,
                    bar.get_y() + bar.get_height() / 2,
                    fmt.format(val), va="center", fontsize=fontsize)
        else:
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + offset_y,
                    fmt.format(val), ha="center", va="bottom", fontsize=fontsize)

# ── Distribución normalizada ──────────────────────────────────────────────────
def pct_reindex(serie, orden=None, fill_value=0):
    """value_counts(normalize) * 100, opcionalmente reindexado."""
    pct = serie.value_counts(normalize=True) * 100
    return pct.reindex(orden, fill_value=fill_value) if orden is not None else pct


# ── Barras dobles (comparación dos grupos) ────────────────────────────────────
def plot_barras_dobles(ax, categorias, valores_a, valores_b,
                       label_a, label_b,
                       color_a="#D85A30", color_b="#1D9E75",
                       width=0.4, rotation=15, fontsize=8, fmt="{:.1f}"):
    
    x = np.arange(len(categorias))
    bars_a = ax.bar(x - width / 2, valores_a, width,
                    label=label_a, color=color_a, alpha=0.8, edgecolor="white")
    bars_b = ax.bar(x + width / 2, valores_b, width,
                    label=label_b, color=color_b, alpha=0.8, edgecolor="white")
    anotar_barras(ax, bars_a, valores_a, fmt=fmt, offset_y=0.3, fontsize=fontsize)
    anotar_barras(ax, bars_b, valores_b, fmt=fmt, offset_y=0.3, fontsize=fontsize)
    ax.set_xticks(x)
    ax.set_xticklabels([str(c)[:20] for c in categorias], rotation=rotation,
                       ha="right", fontsize=fontsize)
    ax.legend(fontsize=fontsize)

