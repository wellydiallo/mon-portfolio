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

st.write("---")
st.header("📈 Data Analysis & Strategic Visualizations")

# 1. Monthly Sales Trend
st.subheader("1. Monthly Sales Trend")
st.image("5.png", caption="Sales peaked in 2017-2018. The sudden drop reflects the dataset's end date.")
st.write("Insight: Seasonality helps in planning inventory and marketing campaigns.")

# 2. Payment Distribution
st.subheader("2. Payment Methods")
st.image("2.png", caption="73.9% of customers use credit cards.")
st.write("Insight: Credit cards are the dominant payment method, reflecting Brazilian purchasing habits.")

# 3. Installment Distribution
st.subheader("3. Installment Plans (The Credit Tool)")
st.image("1.png", caption="Most users pay in 1 installment, but a significant portion uses 2-10 installments.")
st.write("Insight: Credit flexibility is a key driver for conversion. Offering interest-free installments is essential.")

# 4. Top 10 Product Categories (Revenue Share)
st.subheader("4. Top Revenue Categories")
st.image("4.png", caption="Top categories like Health Beauty and Watches drive the majority of revenue.")
st.write("Insight: Focus marketing budget and inventory efforts on these high-performing categories.")

# 5. Top 10 Most Active Customers
st.subheader("5. Active Customer Analysis")
st.image("3.png", caption="The distribution of top customers by order count.")

# --- LE POINT STRATÉGIQUE ---
st.warning("""
**💡 Strategic Limitation:** Looking at the 'Top 10 Active Customers' chart, we can identify *who* they are by ID, but we cannot **act** on this information. 
Without **demographic data** (age, location, interests), we cannot:
- Personalize our communication.
- Implement loyalty programs tailored to specific segments.
- Understand *why* these customers are repeat buyers.

**Next Step:** Integrating demographic and contact data is critical to transform this descriptive analysis into a proactive CRM strategy.
""")


st.write("---")
st.header("🚢 Modélisation prédictive de la survie (Titanic)")

with st.container():
    col1, col2 = st.columns([2, 1])

    with col1:

        st.subheader("1. Problématique & objectifs")

        st.write("""
        Ce projet collaboratif visait à développer un modèle de Machine Learning pour prédire la survie des passagers du Titanic.  
        Au-delà de la simple performance prédictive, l’objectif était d’identifier les déterminants socio-démographiques ayant influencé les chances de survie lors de ce naufrage historique.
        """)

        with st.expander("2. Méthodologie & rigueur technique"):
            st.markdown("""
            **Traitement des données :**  
            Nous avons traité les valeurs manquantes (notamment l’âge) via une imputation intelligente basée sur le titre des passagers (Mr, Mrs, Miss), plutôt qu’une moyenne globale, afin de préserver la cohérence des profils.

            **Feature engineering :**  
            Création de variables stratégiques comme la *taille de la famille* (à partir du nombre de parents/enfants et frères/sœurs).  
            Ces nouvelles variables se sont révélées plus prédictives que les données brutes, soulignant l’importance de l’ingénierie des variables.

            **Modélisation :**  
            Comparaison de plusieurs algorithmes (Régression Logistique, Random Forest, XGBoost), avec sélection du modèle offrant le meilleur compromis entre performance et interprétabilité.
            """)

        with st.expander("3. Résultats & interprétation métier"):
            st.markdown("""
            **Insights :**  
            Le modèle confirme statistiquement que la classe sociale, le sexe et l’âge sont les variables les plus déterminantes dans la survie.

            **Indicateur clé :**  
            L’optimisation a été réalisée sur le **Recall (sensibilité)** afin de minimiser les faux négatifs (cas de survivants non détectés), ce qui était prioritaire dans un contexte de survie.
            """)

        with st.expander("4. Dimension collaborative & soft skills"):
            st.markdown("""
            Ce projet a été réalisé en équipe, avec une gestion de version via Git/GitHub.  
            Cette expérience a permis de renforcer la coordination des étapes de traitement des données et de garantir un pipeline de modélisation structuré, propre et reproductible.
            """)

    with col2:
        st.success("**Résumé projet**")

        st.write("🎯 Objectif : prédire la survie des passagers")
        st.write("🧠 ML : Logistique, Random Forest, XGBoost")
        st.write("📊 KPI : Recall optimisé")
        st.write("🔧 Feature engineering avancé")
        st.write("👥 Travail en équipe (Git/GitHub)")

st.info("""
💡 **Conclusion métier :**  
La survie dépend principalement de facteurs sociaux (classe, sexe, âge), illustrant l’impact des inégalités sociales dans les probabilités de survie.
""")

st.markdown("[🔗 Voir le projet sur GitHub](https://github.com/wellydiallo/titanic-ml-project)")
st.write("---")