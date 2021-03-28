from transformers import BertForMaskedLM, BertTokenizer

model = BertForMaskedLM.from_pretrained("neuralmind/bert-base-portuguese-cased")
tokenizer = BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")

model.save_pretrained("./model")
tokenizer.save_pretrained("./model")