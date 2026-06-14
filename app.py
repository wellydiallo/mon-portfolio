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
    st.image("moi.jpeg", width=150) # Remplace par ta photo plus tard
    st.title("Welly Diallo")
    st.write("📍 Étudiante MSc Data Management")
    st.write("---")
    st.write("📫 **Contact :**")
    st.write("diallowelly620@gmail.com")
    st.write("[LinkedIn](https://www.linkedin.com/in/welly-diallo-ab9283320)")
    st.write("[GitHub](https://github.com/wellydiallo)")
    
    # Bouton pour télécharger le CV
    with open("app.py", "rb") as file: # Remplace par ton fichier CV.pdf plus tard
        st.download_button(label="📄 Télécharger mon CV", data=file, file_name="WellyDiallo_DataAnalyst&BI_2026.pdf")

# --- SECTION PRÉSENTATION ---
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Bonjour, je suis Welly 👋")
    st.subheader("Passionnée par l'extraction de valeur à partir des données.")
    st.write("""
    Future étudiante en **MSc Data Management**. Mon objectif est de comprendre 
    les enjeux complexes des données pour aider à la prise de décision. 
    Bienvenue sur mon espace où je partage mes projets et mes apprentissages !
    """)

# --- MES COMPÉTENCES ---
st.write("---")
st.header("🛠️ Compétences")
c1, c2, c3, c4 = st.columns(4)
with c1: st.info("**Langages** : Python, SQL, R & R Studio, Java")
with c2: st.success("**Data** : Pandas, Numpy, Matplotlib, Seaborn")
with c3: st.warning("**IA** : Scikit-Learn, ML, MCP, OpenAI Code, Dust")
with c4: st.error("**Outils** : Ecxel, Metabase, Git, Streamlit, Jupyter Notebook")

# --- SECTION PROJETS ---
st.header("🚀 Mes Projets Data")

# --- Projet 2 : E-commerce SQL ---
st.write("---")
st.header("📊 E-commerce Data Analysis Project")

# --- CONTEXT & OBJECTIVE ---
with st.container():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Project Overview")
        st.write("""
        This project analyzes raw transactional data from the Brazilian market to extract actionable business insights. 
        It covers the entire data pipeline: from SQL extraction and data cleaning with Pandas, to calculating KPIs and visualizing trends that drive strategic decision-making.
        """)
        
        with st.expander("🛠️ Technical Stack & Methodology"):
            st.markdown("""
            - **SQL:** Complex queries (JOINs, Aggregations, Window Functions).
            - **Python:** Data cleaning, KPI calculation, and statistical analysis.
            - **Visualization:** Matplotlib & Seaborn for pattern recognition.
            - **Business Logic:** Seasonality analysis, customer segmentation, and payment habit profiling.
            """)
            
    with col2:
        st.success("**Key Metrics:**")
        st.metric(label="Average Order Value", value="154.1 $")
        st.write("🗓️ **Seasonality:** Peak activity in May, July, and August.")

st.write("---")

# --- COMPREHENSIVE BUSINESS ANALYSIS ---
st.subheader("Strategic Business Insights")

c1, c2 = st.columns(2)

with c1:
    st.write("**1. Product Strategy & Growth**")
    st.info("""
    My analysis revealed a strong correlation between product variety and sales volume. Top-performing categories, such as *Bed, Table & Bath*, succeed by offering a wide assortment. 
    **Recommendation:** Prioritize these "star" categories for inventory planning and targeted advertising to maximize ROI.
    """)
    
    st.write("**2. Payment Ecosystem**")
    st.info("""
    73% of transactions are processed via credit card. The high frequency of installment plans (up to 10 months) confirms that offering interest-free installments is the primary engine for conversion in Brazil, allowing customers to manage their household budgets effectively.
    """)

with c2:
    st.write("**3. Operational Recommendations**")
    st.info("""
    - **Logistics:** Since delivery efficiency directly impacts customer satisfaction, I have calculated delivery performance metrics to identify potential bottlenecks.
    - **Inventory:** Align marketing campaigns with identified seasonal peaks in May, July, and August to optimize stock turnover.
    """)

# --- FUTURE SCOPE: THE PROACTIVE APPROACH ---
st.write("---")
st.subheader("🚀 Future Scope: Data-Driven Evolution")
st.write("""
To move from descriptive to predictive analysis, I propose the following roadmap:
""")

col_a, col_b = st.columns(2)

with col_a:
    st.write("📍 **Geographic & Demographic Enrichment**")
    st.write("By integrating location data, we can optimize regional logistics costs and develop hyper-local marketing campaigns.")

with col_b:
    st.write("🤖 **CRM & Seller Retention Strategy**")
    st.write("Linking seller performance to contact data enables an automated CRM system: providing personalized monthly reports and loyalty programs for top-tier partners.")

st.markdown("[🔗 View Project on GitHub](https://github.com/wellydiallo/Personal-project-e-commerce-sales-analysis-sql)")
st.write("---")


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

