import re
import streamlit as st

st.title("Générateur de code Amadeus intelligent")

# Zone de texte pour coller l'exemple de dossier/ligne Amadeus
pnr_text = st.text_area(
    "Collez votre ligne de vol Amadeus ici :",
    value="2 VT 948 L 12AUG 3 PPTTUB SA1  1 0530 0710 *1A/E*",
)

if st.button("Générer le code Amadeus"):
    try:
        # Expression régulière flexible : 
        # Elle cherche la compagnie, le vol, la classe, la date, le nombre de passagers, le trajet et le statut (ex: SA1 ou HK2)
        pattern = r"([A-Z0-9]{2})\s+(\d+)\s+([A-Z])\s+(\d{2}[A-Z]{3})\s+(\d+)\s+([A-Z]{6})\s+([A-Z]{2})(\d+)"
        match = re.search(pattern, pnr_text)

        if match:
            airline = match.group(1)      # ex: VT
            flight_num = match.group(2)   # ex: 948
            cls = match.group(3)          # ex: L
            date = match.group(4)         # ex: 12AUG
            # match.group(5) est le '3' intermédiaire si besoin
            route = match.group(6)        # ex: PPTTUB
            status_letters = match.group(7) # ex: SA
            pax_count = match.group(8)    # ex: Le chiffre après le statut (ex: 1)

            # Construction du code final : SS + Compagnie + Vol + Classe + Date + Trajet + Nombre final
            amadeus_code = f"SS{airline}{flight_num}{cls}{date}{route}{pax_count}"

            st.success("Code généré avec succès !")
            st.subheader("Résultat à copier-coller :")
            st.code(amadeus_code, language="text")
        else:
            st.error("Impossible de reconnaitre le format de la ligne. Vérifiez votre texte.")

    except Exception as e:
        st.error(f"Une erreur est survenue lors du traitement : {e}")
