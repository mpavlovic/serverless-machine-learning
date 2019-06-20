print('container start')

try:
    import unzip_requirements
except ImportError as error:
    pass

print('unzipped')

import json
import en_core_web_sm

MODEL = en_core_web_sm.load()
print('model loaded')

def create_ner_spans(text):
    doc = MODEL(text)
    spans = []
    for ent in doc.ents:
        span = {
            'start': ent.start_char,
            'end': ent.end_char,
            'type': ent.label_
        }
        spans.append(span)
    return spans


def handle_request(event, context):
    text = event['body']
    print(text)
    spans = []
    if text is not None:
        spans = create_ner_spans(text)
    print(spans)

    body = {
        'spans': spans
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    return response