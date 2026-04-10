from src.orchestrator.pipeline import Orchestrator

if __name__ == "__main__":
    pipeline = Orchestrator(
        data_path="data/sample.json",
        model_name="Helsinki-NLP/opus-mt-fr-en",
        output_dir="output"
    )
    pipeline.run()