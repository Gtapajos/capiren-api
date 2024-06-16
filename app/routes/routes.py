from flask import Blueprint, request, jsonify
from app.utils.pdf_proccessing import PDFProcessing
from app.models.ner_model import NerModel

ner_app = Blueprint('ner_routes', __name__)

@ner_app.route('/labels', methods=['GET'])
def get_labels():
    text = request.json['text']
    category = request.json['category']
    model = request.json['model']

    ner = NerModel()

    ner.load_model(category, model)

    response = ner.get_inference(text)
    
    return jsonify(response)

@ner_app.route('/pdf_text', methods=['GET'])
def get_pdf_text():
    
    pdf_file = request.files['file']

    pdf_proc = PDFProcessing()

    pdf_proc.set_file(pdf_file)

    return jsonify({'extracted_text': pdf_proc.get_text()})
