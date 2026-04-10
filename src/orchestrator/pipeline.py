class Orchestrator:
    def __init__(self, data_path, model_name, output_dir):
        self.data_path = data_path
        self.model_name = model_name
        self.output_dir = output_dir

    def run(self):
        print("Pipeline started...")

        # 1. load data (fake pour l’instant)
        data = ["bonjour", "je suis étudiant"]

        # 2. fake translation (sera remplacé après)
        translations = [d + " -> translated" for d in data]

        # 3. evaluation fake BLEU
        score = 0.75

        print("Translations:", translations)
        print("BLEU score:", score)

        print("Pipeline finished ✔")