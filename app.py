import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Welly Diallo | Portfolio Data & IA", layout="wide")

# --- STYLE CSS (Pour personnaliser un peu) ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Barre latérale) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6840/6840478.png", width=150) # Remplace par ta photo plus tard
    st.title("Welly Diallo")
    st.write("📍 Étudiante en IA & Big Data")
    st.write("---")
    st.write("📫 **Contact :**")
    st.write("welly.diallo@email.com")
    st.write("[LinkedIn](https://linkedin.com/in/ton-profil)")
    st.write("[GitHub](https://github.com/wellydiallo)")
    
    # Bouton pour télécharger le CV
    with open("app.py", "rb") as file: # Remplace par ton fichier CV.pdf plus tard
        st.download_button(label="📄 Télécharger mon CV", data=file, file_name="CV_Welly_Diallo.pdf")

# --- SECTION PRÉSENTATION ---
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Bonjour, je suis Welly 👋")
    st.subheader("Passionnée par l'extraction de valeur à partir des données.")
    st.write("""
    Je suis actuellement étudiante en **IA et Big Data**. Mon objectif est de comprendre 
    les enjeux complexes des données pour aider à la prise de décision. 
    Bienvenue sur mon espace où je partage mes projets et mes apprentissages !
    """)

# --- MES COMPÉTENCES ---
st.write("---")
st.header("🛠️ Compétences")
c1, c2, c3, c4 = st.columns(4)
with c1: st.info("**Langages** : Python, SQL")
with c2: st.success("**Data** : Pandas, Numpy")
with c3: st.warning("**IA** : Scikit-Learn, ML")
with c4: st.error("**Outils** : Git, Streamlit")

# --- SECTION PROJETS ---
st.header("🚀 Mes Projets Data")

# Projet 1 : Titanic
with st.container():
    st.subheader("🚢 Titanic : Prédiction de survie")
    st.write("**Objectif :** Prédire la survie des passagers via Machine Learning.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        **Outils :** Python, Pandas, Scikit-learn, Seaborn
        **Résultats :** 94% de précision avec KNN.
        """)
        st.markdown("[🔗 Voir le code sur GitHub](https://github.com/wellydiallo/Projet-Titanic)")
    
    with col2:
        # Utilise un expander pour les détails techniques
        with st.expander("Voir la méthodologie"):
            st.write("""
            1. **Nettoyage :** Traitement des valeurs manquantes.
            2. **Analyse :** Étude des corrélations âge/sexe/classe.
            3. **Feature Engineering :** Création de nouvelles variables pertinentes.
            4. **Modélisation :** Comparaison entre Régression Logistique et KNN.
            """)

st.write("") # Espace

# Projet 2
col_p2_img, col_p2_txt = st.columns([1, 2])
with col_p2_img:
    st.image("https://placehold.co/400x250?text=Analyse+SQL")
with col_p2_txt:
    st.subheader("Optimisation de base de données SQL")
    st.write("Nettoyage et analyse d'un dataset de ventes retail pour identifier les produits les plus rentables.")
    st.markdown("[Voir le code sur GitHub](https://github.com/wellydiallo)")
