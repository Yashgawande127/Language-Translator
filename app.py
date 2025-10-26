from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Language mapping for deep-translator
LANGUAGES = {
    'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
    'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
    'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech',
    'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian',
    'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician',
    'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
    'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi',
    'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian',
    'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada',
    'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz',
    'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish',
    'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese',
    'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali',
    'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish',
    'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan',
    'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi',
    'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish',
    'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil',
    'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu',
    'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa',
    'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'
}

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/languages', methods=['GET'])
def get_languages():
    """Get available languages"""
    try:
        # Convert language codes to a more user-friendly format
        language_list = []
        for code, name in LANGUAGES.items():
            language_list.append({
                'code': code,
                'name': name.title()
            })
        
        # Sort by name for better user experience
        language_list.sort(key=lambda x: x['name'])
        
        return jsonify({
            'success': True,
            'languages': language_list
        })
    except Exception as e:
        logger.error(f"Error getting languages: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Failed to retrieve languages'
        }), 500

@app.route('/api/translate', methods=['POST'])
def translate_text():
    """Translate text from source to target language"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
            
        text = data.get('text', '').strip()
        source_lang = data.get('source', 'auto')
        target_lang = data.get('target', 'en')
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'No text provided for translation'
            }), 400
            
        if len(text) > 5000:
            return jsonify({
                'success': False,
                'error': 'Text too long. Maximum 5000 characters allowed.'
            }), 400
        
        # Perform translation using deep-translator
        if source_lang == 'auto':
            # Auto-detect language
            try:
                detected_lang = detect(text)
            except LangDetectException:
                detected_lang = 'en'  # Default to English if detection fails
            translator = GoogleTranslator(source=detected_lang, target=target_lang)
            translated_text = translator.translate(text)
        else:
            # Translate with specified source language
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            translated_text = translator.translate(text)
            detected_lang = source_lang
        
        # Get language names
        detected_lang_name = LANGUAGES.get(detected_lang, detected_lang).title()
        target_lang_name = LANGUAGES.get(target_lang, target_lang).title()
        
        return jsonify({
            'success': True,
            'translated_text': translated_text,
            'detected_language': {
                'code': detected_lang,
                'name': detected_lang_name
            },
            'target_language': {
                'code': target_lang,
                'name': target_lang_name
            },
            'original_text': text
        })
        
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Translation failed: {str(e)}'
        }), 500

@app.route('/api/detect', methods=['POST'])
def detect_language():
    """Detect the language of given text"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
            
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'No text provided for detection'
            }), 400
        
        # Detect language using langdetect
        try:
            detected_lang = detect(text)
        except LangDetectException:
            detected_lang = 'en'  # Default to English if detection fails
            
        language_name = LANGUAGES.get(detected_lang, detected_lang).title()
        
        return jsonify({
            'success': True,
            'detected_language': {
                'code': detected_lang,
                'name': language_name,
                'confidence': 0.9  # deep-translator doesn't provide confidence scores
            }
        })
        
    except Exception as e:
        logger.error(f"Detection error: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Language detection failed: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)