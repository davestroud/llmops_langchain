from kfp import dsl
from kfp.components import load_component_from_text

@dsl.pipeline(name="LLM Ops Pipeline")
def llm_ops_pipeline():
    preprocess_op = load_component_from_text("""
    name: Preprocess Data
    implementation:
      container:
        image: my-docker-repo/preprocess-image:latest
        command: ["python", "preprocess.py"]
    """)
    
    train_op = load_component_from_text("""
    name: Train Model
    implementation:
      container:
        image: my-docker-repo/train-image:latest
        command: ["python", "train.py"]
    """)

    preprocess_task = preprocess_op()
    train_task = train_op(preprocess_task.outputs['processed_data'])

if __name__ == "__main__":
    from kfp.client import Client
    client = Client()
    client.create_run_from_pipeline_func(llm_ops_pipeline, arguments={})
