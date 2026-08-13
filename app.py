import re
import streamlit as st

st.title("HL iso SA")

pnr_text = st.text_area(
    "Collez votre ligne de vol Amadeus ici :",
    value="2 VT 964 M 16AUG 3 PPTHOI SA1  1 0530 0710 *1A/E*",
)

if st.button("HL ISO SA"):
    try:
        pattern = r"([A-Z0-9]{2})\s+(\d+)\s+([A-Z])\s+(\d{2}[A-Z]{3})\s+(\d+)\s+([A-Z]{6})\s+([A-Z]{2})(\d+)"
        match = re.search(pattern, pnr_text)

        if match:
            airline = match.group(1)      
            flight_num = match.group(2)   
            cls = match.group(3)          
            date = match.group(4)         
            route = match.group(6)        
            status_letters = match.group(7) 
            pax_count = match.group(8)    

            # Modification ici : .lower() pour les minuscules et ajout de LF
            amadeus_code = f"SS{airline}{flight_num}{cls.lower()}{date.lower()}{route.lower()}LF{pax_count}"

            st.success("Code généré avec succès !")
            st.subheader("Résultat à copier-coller :")
            st.code(amadeus_code, language="text")
        else:
            st.error("Impossible de reconnaitre le format de la ligne. Vérifiez votre texte.")

    except Exception as e:
        st.error(f"Une erreur est survenue lors du traitement : {e}")
