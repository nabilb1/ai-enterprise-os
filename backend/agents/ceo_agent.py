from services.llm_service import ask_llm
class CEOAgent:

    def run(self, question: str):

        prompt = f"""
Tu es un Directeur Général virtuel expert en :
- Stratégie d'entreprise
- Finance
- RH
- Management
- Transformation digitale

Question :
{question}

Réponds avec la structure suivante :

1. Analyse
2. Risques
3. Opportunités
4. Recommandations
"""

        return ask_llm(prompt)
