
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

ORIG_MODEL = "XformAI-india/qwen-1.7b-coder"

bnb = BitsAndBytesConfig(load_in_4bit=True,
                         bnb_4bit_quant_type="nf4",
                         bnb_4bit_compute_dtype="bfloat16",
                         bnb_4bit_use_double_quant=True)

model = AutoModelForCausalLM.from_pretrained(
    ORIG_MODEL,
    device_map="auto", trust_remote_code=True,
    quantization_config=bnb
)

NEW_REPO   = "kenshi777/qwen-1.7b-coder-4bit"

model.save_pretrained(NEW_REPO, safe_serialization=True, push_to_hub=True)
AutoTokenizer.from_pretrained(ORIG_MODEL).save_pretrained(NEW_REPO, push_to_hub=True)