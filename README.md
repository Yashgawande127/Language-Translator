# Language Translator

A modern web-based language translator built with Python Flask and Google Translate API. Supports 100+ languages with auto-detection, real-time translation, and a beautiful responsive interface.

## Features

- 🌍 **100+ Languages**: Support for major world languages and dialects
- 🔍 **Auto-Detection**: Automatically detects the source language
- 🚀 **Real-time Translation**: Fast and accurate translations
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 💾 **Copy to Clipboard**: Easy copying of translations
- ⇄ **Language Swapping**: Quick language pair swapping
- 📊 **Character Counter**: Visual feedback on text length
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations

## Installation

1. **Clone or download the project**
   ```
   cd "Language Translator"
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
   Or install individually:
   ```
   pip install flask googletrans==4.0.0-rc1 flask-cors
   ```

## Usage

1. **Start the application**
   ```
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

3. **Start translating!**
   - Enter text in the input area
   - Select source and target languages (or use auto-detect)
   - Click "Translate" or press Ctrl+Enter
   - Copy the translation with the copy button

## API Endpoints

The application also provides REST API endpoints:

### GET /api/languages
Returns all available languages with codes and names.

### POST /api/translate
Translates text from source to target language.
```json
{
  "text": "Hello world",
  "source": "en",
  "target": "es"
}
```

### POST /api/detect
Detects the language of given text.
```json
{
  "text": "Bonjour le monde"
}
```

## Project Structure

```
Language Translator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    └── index.html        # Frontend interface
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Translation**: Google Translate API via googletrans library
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Modern CSS with gradients and animations
- **Cross-Origin**: Flask-CORS for API access

## Features in Detail

### Language Support
- Over 100 languages supported
- Automatic language detection
- Language names displayed in user-friendly format

### User Interface
- Modern gradient design
- Responsive layout for all devices
- Character counter with visual warnings
- Loading indicators and error messages
- Success notifications with auto-hide

### Translation Features
- Real-time translation
- Character limit (5000) with validation
- Detected language display
- Easy language swapping
- Copy to clipboard functionality

## Keyboard Shortcuts

- **Ctrl + Enter**: Translate text
- **Escape**: Clear messages

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Troubleshooting

### Common Issues

1. **Translation not working**
   - Check your internet connection
   - Ensure Google Translate service is accessible
   - Try refreshing the page

2. **Languages not loading**
   - Restart the application
   - Check console for error messages

3. **Copy to clipboard not working**
   - Ensure HTTPS or localhost
   - Check browser permissions

### Error Messages

The application provides clear error messages for:
- Network connectivity issues
- Invalid input (empty text, too long text)
- Translation service errors
- Language detection failures

## Development

To modify or extend the application:

1. **Backend (app.py)**: Add new API endpoints or modify translation logic
2. **Frontend (templates/index.html)**: Update the user interface or add new features
3. **Styling**: Modify the CSS within the HTML file

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!

## Support

For support, please check the troubleshooting section or create an issue in the project repository.