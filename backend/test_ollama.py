from services.llm_service import ask_llm

response = ask_llm(
    "Explique en une phrase ce qu'est AI Enterprise OS."
)

print(response)