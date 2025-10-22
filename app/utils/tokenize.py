import tiktoken

MODEL_TOKENIZERS = {
    "fluffy/l3-8b-stheno-v3.2:q8_0": {"tokenizer": "cl100k_base", "context": 128000},
    "HammerAI/mn-mag-mell-r1:12b-q4_K_M": {"tokenizer": "cl100k_base", "context": 1000000},
    "wizardlm-uncensored:13b-llama2-q8_0": {"tokenizer": "cl100k_base", "context": 4000},
    "HammerAI/dans-personalityengine-v1.3.0:24b-q6_K-i1": {"tokenizer": "cl100k_base", "context": 128000},
    "mattw/llama2-13b-tiefighter:latest": {"tokenizer": "cl100k_base", "context": 4000},
    "HammerAI/rocinante-v1.1:12b-q4_K_M": {"tokenizer": "cl100k_base", "context": 1000000},
    "HammerAI/cydonia-v3.1:24b-q8_0": {"tokenizer": "cl100k_base", "context": 128000}
}

def count_tokens(text: str, model: str = "default") -> int:
    encoding_name = MODEL_TOKENIZERS.get(model, {}).get("tokenizer", "cl100k_base")
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))

def get_model_max_context(model: str = "default") -> int:
    return MODEL_TOKENIZERS.get(model, {}).get("context", -1)
