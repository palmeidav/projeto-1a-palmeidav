from utils import load_data, load_template, add, build_response
from urllib.parse import unquote_plus
def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  
        parts = request.split('\n\n')
        body = parts[1]
        parameters = {}
        for value in body.split('&'):
            key, valor = value.split('=')
            parameters[key] = unquote_plus(valor)
        titulo = parameters.get('titulo', '')
        detalhes = parameters.get('detalhes', '')
        add(titulo, detalhes)  
        return build_response(code=303, reason='See Other', headers='Location: /')
    
    entrando_template = load_template('components/note.html')
    notes_li = [
        entrando_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)
    return build_response(body=load_template('index.html').format(notes=notes))
