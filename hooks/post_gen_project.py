import subprocess
print("Projet généré avec succès !")
# Tentative de formatage automatique (si black est installé)
try:
subprocess.run(["black", "."], check=False)
print(" Code formaté avec black.")
except Exception:
print("Black non installé, formatage ignoré.")
print("Votre projet est prêt à l’emploi.")
