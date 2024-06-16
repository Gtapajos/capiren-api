from transformers import AutoTokenizer
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

class NerModel():
    def __init__(self):
        self.__tokenizer = ""
        self.__model = ""

    def load_model(self, category, model_name):
        model = self.__assign_model(category, model_name)
        self.__tokenizer = AutoTokenizer.from_pretrained(model)
        self.__model = AutoModelForTokenClassification.from_pretrained(model)
            
    def get_inference(self, text):
        nlp = pipeline("ner", model=self.__model, tokenizer=self.__tokenizer, aggregation_strategy="first")

        ner_results = nlp(text)
        
        filtered_results = []
        expected_keys = ['entity_group', 'word']
        for result in ner_results:
            filtered_result = {key: result[key] for key in expected_keys if key in result}
            filtered_results.append(filtered_result)

        ner_results = filtered_results
        
        return ner_results
    
    def __assign_model(self, category, model_name):
        model = f"GuiTap/{model_name}-finetuned-ner"
        if category == 0:
            return model + '-harem'
        elif category == 1:
            return model + '-lenerBR'
        elif category == 2:
            return model + '-geocorpus'
