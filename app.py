import streamlit as st
from manim import * 
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math


st.set_page_config(layout="wide")
st.markdown(r"# $\mathbb{Z}_n$ Visualizer")

order = st.number_input("Enter the order of the group",min_value=1,step=1)

MANIM_COLORS = {
    "YELLOW": YELLOW,
    "BLUE": BLUE,
    "RED": RED,
    "GREEN": GREEN,
    "ORANGE": ORANGE,
    "PURPLE": PURPLE,
    "PINK": PINK,
    "TEAL": TEAL,
    "GOLD": GOLD,
    "MAROON": MAROON,
    "WHITE": WHITE,
    "BLACK": BLACK,
}

color_1_name = st.selectbox(
    "Choose first color",
    list(MANIM_COLORS.keys())
)

color_2_name = st.selectbox(
    "Choose second color",
    list(MANIM_COLORS.keys())
)

color_1 = MANIM_COLORS[color_1_name]
color_2 = MANIM_COLORS[color_2_name]
colors = color_gradient([color_1, color_2], int(order))




button_1 = st.button("Show color bar")
if button_1:
    st.write("Your colors :")
    fig, ax = plt.subplots(figsize=(10, 2))
    for i, color in enumerate(colors):
        ax.add_patch(
            Rectangle((i, 0), 1, 1, color=color.to_hex())
        )
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)
    plt.close(fig)


button_2 = st.button("Show Cayley Table")
if button_2:

    col1, col2 = st.columns((1,1))
    with col1:
        n = int(order)
        color_maps = {
            color.to_hex(): i 
            for i, color in enumerate(colors)
        }
        value_to_color = {
            round(v, 1): k
            for k, v in color_maps.items()
        }
        compositions = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(value_to_color[(i + j) % n])
            compositions.append(row)
        n = len(colors)

        fig, ax = plt.subplots(figsize=(4,4))

        for i in range(n):
            for j in range(n):
                color = compositions[i][j]

                ax.add_patch(
                    Rectangle((j, n-1-i), 1, 1,
                              facecolor=color,
                              edgecolor='black')
                )
                ax.text(
                    j + 0.5,
                    n - 1 - i + 0.5,
                    str((i + j) % n),
                    ha='center',
                    va='center',
                    fontsize=max(2, 12 - n//2)
                )

        ax.set_xticks([i + 0.5 for i in range(n)])
        ax.set_xticklabels(range(n))

        ax.set_yticks([i + 0.5 for i in range(n)])
        ax.set_yticklabels(range(n-1, -1, -1))

        ax.set_xlabel("Second Color")
        ax.set_ylabel("First Color")
        ax.set_title(
                rf"Color Composition (Cayley Table of $\mathbb{{Z}}_{{{n}}}$)"
            )
        ax.set_xlim(0, n)
        ax.set_ylim(0, n)
        ax.set_aspect('equal')
        st.pyplot(fig, use_container_width=False)
    
    with col2:
        st.header("Some Properties")
    
        generators = [k for k in range(1, n) if math.gcd(k, n) == 1]
    
        st.latex(r"e = 0")
    
        st.latex(r"\mathbb{Z}_{%d}\ \text{is a cyclic group}" % n)
    
        st.latex(
            r"\mathrm{Generators}\left(\mathbb{Z}_{%d}\right)"
            r"=\left\{%s\right\}"
            % (
                n,
                ", ".join(map(str, generators))
            )
        )