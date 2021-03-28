from transformers import BertForMaskedLM, BertTokenizer

model = BertForMaskedLM.from_pretrained("neuralmind/bert-base-portuguese-cased")
tokenizer = BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")

model.save_pretrained("/home/models/neuralmind")
tokenizer.save_pretrained("/home/models/neuralmind")