import re
import streamlit as st

st.title("Générateur de code Amadeus intelligent")

# Zone de texte pour coller l'exemple de dossier/ligne Amadeus
pnr_text = st.text_area(
    "Collez votre ligne de vol Amadeus ici :",
    value="3   VT 171 L 18AUG 2 PPTNKP HK2",
)

if st.button("Générer le code Amadeus"):
    try:
        # Expression régulière pour capturer les éléments clés de la ligne de vol
        pattern = r"([A-Z0-9]{2})\s+(\d+)\s+([A-Z])\s+(\d{2}[A-Z]{3})\s+(\d+)\s+([A-Z]{6})"
        match = re.search(pattern, pnr_text)

        if match:
            airline = match.group(1)  # ex: VT
            flight_num = match.group(2)  # ex: 171
            cls = match.group(3)  # ex: L (corrigé ici)
            date = match.group(4)  # ex: 18AUG
            pax_count = match.group(5)  # ex: 2 (nombre de places)
            route = match.group(6)  # ex: PPTNKP

            # Construction du code final basé sur votre modèle en couleur :
            # SS + Compagnie + Vol + Classe + Date + Trajet + Nombre
            amadeus_code = (
                f"SS{airline}{flight_num}{cls}{date}{route}{pax_count}"
            )

            st.success("Code généré avec succès !")
            st.subheader("Résultat à copier-coller :")
            st.code(amadeus_code, language="text")
        else:
            st.error(
                "Impossible de reconnaitre le format de la ligne. Vérifiez votre texte."
            )

    except Exception as e:
        st.error(f"Une erreur est survenue lors du traitement : {e}")
