# 🤖 Jarvis AI Assistant

![Jarvis AI](Frontend/Graphics/Jarvis.gif)

## 🌟 Overview

Jarvis AI is a powerful voice-controlled personal assistant designed to help you with a wide range of tasks. Inspired by Iron Man's JARVIS, this application can answer your questions, search the internet for real-time information, control your computer, play music, generate images, and much more.

## 🔍 Current State Gap Identification

Current digital assistants often fall short in several key areas:

- **Limited Integration**: Most assistants operate within closed ecosystems
- **Privacy Concerns**: Cloud-based solutions raise data privacy issues
- **Contextual Understanding**: Many systems struggle with complex, multi-turn conversations
- **Customization Limitations**: End users have minimal control over functionality
- **Responsiveness**: Network-dependent assistants can be slow to respond

Jarvis AI aims to address these gaps by providing a more integrated, responsive, and customizable experience with an architecture that balances cloud capabilities with local processing.

## 🎯 Problem Definition

The project addresses several key challenges in personal AI assistants:

1. **Accessibility**: Making advanced AI capabilities accessible to everyday users
2. **Multifunctionality**: Creating a unified interface for diverse digital tasks
3. **Response Quality**: Ensuring responses are both accurate and helpful
4. **System Integration**: Interacting with various applications and services
5. **User Experience**: Minimizing friction in human-AI interaction

## ✨ Features

- **🎙️ Voice Interaction** - Natural voice commands and responses
- **🧠 Intelligent Query Processing** - Automatically determines if your question needs real-time data or can be answered from existing knowledge
- **🖥️ System Automation** - Open/close applications, control your computer
- **🔍 Web Search** - Real-time information from the internet
- **🎵 Media Control** - Play music and videos
- **🖼️ Image Generation** - Create images based on your descriptions
- **💬 Natural Conversation** - Engage in human-like conversations
- **👁️ Screen Analysis** - Analyze and describe what's happening on your screen using Google's Gemini Vision AI
- **🤖 Camera Analysis** - Analyze your webcam feed using Google's Gemini Vision AI

![Jarvis AI](Frontend/Graphics/Jarvis.gif)

## 🌟 Overview

Jarvis AI is a powerful voice-controlled personal assistant designed to help you with a wide range of tasks. Inspired by Iron Man's JARVIS, this application can answer your questions, search the internet for real-time information, control your computer, play music, generate images, and much more.

## 🔍 Current State Gap Identification

Current digital assistants often fall short in several key areas:

- **Limited Integration**: Most assistants operate within closed ecosystems
- **Privacy Concerns**: Cloud-based solutions raise data privacy issues
- **Contextual Understanding**: Many systems struggle with complex, multi-turn conversations
- **Customization Limitations**: End users have minimal control over functionality
- **Responsiveness**: Network-dependent assistants can be slow to respond

Jarvis AI aims to address these gaps by providing a more integrated, responsive, and customizable experience with an architecture that balances cloud capabilities with local processing.

## 🎯 Problem Definition

The project addresses several key challenges in personal AI assistants:

1. **Accessibility**: Making advanced AI capabilities accessible to everyday users
2. **Multifunctionality**: Creating a unified interface for diverse digital tasks
3. **Response Quality**: Ensuring responses are both accurate and helpful
4. **System Integration**: Interacting with various applications and services
5. **User Experience**: Minimizing friction in human-AI interaction

## ✨ Features

- **🎙️ Voice Interaction** - Natural voice commands and responses
- **🧠 Intelligent Query Processing** - Automatically determines if your question needs real-time data or can be answered from existing knowledge
- **🖥️ System Automation** - Open/close applications, control your computer
- **🔍 Web Search** - Real-time information from the internet
- **🎵 Media Control** - Play music and videos
- **🖼️ Image Generation** - Create images based on your descriptions
- **💬 Natural Conversation** - Engage in human-like conversations
- **👁️ Screen Analysis** - Analyze and describe what's happening on your screen using Google's Gemini Vision AI

## 🛠️ Technology Stack

- **Frontend**: PyQt5 for the graphical user interface
- **Backend**:
  - **AI Models**: Groq and Cohere APIs for natural language processing, Google Gemini for vision AI
  - **Speech Processing**: Web Speech API for speech recognition, Edge TTS for text-to-speech
  - **Web Integration**: Selenium for web automation
  - **Media**: Pygame for audio playback
  - **Computer Vision**: OpenCV and MSS for screen capture and analysis

## ⚙️ Performance Characteristics and Requirements

### Performance

- **Response Time**: Typically under 2 seconds for commands, 3-5 seconds for knowledge queries
- **Memory Usage**: ~200MB base, scaling to ~500MB during operation
- **CPU Utilization**: Moderate during speech recognition, low during idle
- **Network**: Stable internet connection (1Mbps+ recommended)
- **Disk Space**: Minimal (<100MB) excluding Python and dependencies

### Hardware Requirements

- **Processor**: Intel Core i3/AMD Ryzen 3 or better
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 1GB free space
- **Audio**: Working microphone and speakers/headphones
- **Operating System**: Windows 10/11 (primary support), adaptable for Linux/macOS

## 📋 Requirements

- **Python 3.10.10** (recommended)
- The following packages:

```
python-dotenv
groq
AppOpener
pywhatkit
bs4
selenium
pillow
rich
requests
keyboard
cohere
googlesearch-python
mtranslate
pygame
edge-tts
PyQt5
webdriver-manager
google-generativeai
opencv-python
numpy
mss
playsound
SpeechRecognition
```

## 🚀 Installation

1. Install Python 3.10.10 from [python.org](https://www.python.org/downloads/release/python-31010/)

2. Clone the repository:
   ```
   git clone https://github.com/atharva-shinde7/JARVIS-AI.git
   cd JARVIS-AI
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r Requirements.txt
   ```

4. Create a `.env` file with the following variables:
   ```
   CohereAPIKey = your_cohere_api_key
   Username = Your Name
   Assistantname = Jarvis
   GroqAPIKey = your_groq_api_key
   InputLanguage = en
   AssistantVoice = en-CA-LiamNeural
   HuggingFaceAPIKey = your_huggingface_api_key
   GeminiAPIKey = your_gemini_api_key
   ```

## 🚢 Deployment Considerations

When deploying Jarvis AI, consider the following:

### Environment Setup

- **Python Environment**: Preferably isolate in a virtual environment
- **API Keys**: Secure storage of API keys (consider environment variables)
- **Browser Dependencies**: MS Edge WebDriver for speech recognition

### Scaling Options

- **Local Network Deployment**: Can be deployed on a home server
- **API Usage Limits**: Monitor usage of third-party APIs
- **Data Storage**: Configure chat history retention based on storage constraints

### Security Considerations

- **API Key Protection**: Store keys securely, not in source code
- **Permission Management**: Limit system command execution scope
- **Data Privacy**: Local storage of conversation history

## 🎮 Usage

To start Jarvis AI:

```
python Main.py
```

### Voice Commands Examples:

- **General Questions**: "Who was Albert Einstein?" or "How do stars form?"
- **Real-time Information**: "What's today's news?" or "Who is the current Prime Minister of India?"
- **Open Applications**: "Open Chrome" or "Open Notepad"
- **Close Applications**: "Close Spotify" or "Close Calculator"
- **Play Music**: "Play Shape of You" or "Play songs by Ed Sheeran"
- **Generate Images**: "Generate an image of a mountain landscape"
- **Web Search**: "Google search for AI tutorials" or "YouTube search for cooking recipes"
- **Screen Analysis**: "Analyze my screen" or "Analyze screen" - Jarvis will enter screen analysis mode and listen for specific screen analysis commands
- **Camera Analysis**: "Analyze camera" or "What's on my camera?" - Jarvis will analyze your webcam feed

## 🧩 Project Structure

```
Jarvis AI/
│
├── Main.py                  # Main application entry point
│
├── Frontend/                # GUI and user interface components
│   ├── GUI.py               # Main GUI implementation
│   ├── Graphics/            # Icons and visual assets
│   └── Files/               # Temporary files for UI state
│
├── Backend/                 # Core functionality modules
│   ├── Model.py             # Decision-making model (Cohere)
│   ├── Chatbot.py           # Conversational AI (Groq)
│   ├── SpeechToText.py      # Voice recognition
│   ├── TextToSpeech.py      # Voice synthesis
│   ├── RealtimeSearchEngine.py # Web search functionality
│   ├── Automation.py        # System control functions
│   ├── ImageGeneration.py   # AI image generation
│   └── screen_analysis.py   # Screen analysis using Google Gemini Vision AI
│
├── Data/                    # Storage for conversation history and settings
│
├── .env                     # Environment variables and API keys
│
└── Requirements.txt         # Python dependencies
```

## 🔄 How It Works

1. **Voice Input**: The system listens for your voice commands using the web speech API.
2. **Query Analysis**: Jarvis uses the First Layer Decision-Making Model to classify your query.
3. **Task Execution**:
   - For general knowledge questions, it uses the Groq LLM.
   - For real-time information, it searches the web.
   - For commands, it performs the requested action.
   - For screen analysis, it activates the dedicated screen analysis module.
   - For camera analysis, it activates the dedicated camera analysis module.
4. **Response**: Jarvis responds both visually (text on screen) and audibly (text-to-speech).

## ⚠️ Limitations Discussion

Jarvis AI, while powerful, has several limitations to be aware of:

1. **API Dependency**: Requires active internet for many functions
2. **Speech Recognition Accuracy**: May struggle in noisy environments
3. **Language Support**: Primary support for English, limited multilingual capabilities
4. **Resource Consumption**: Browser-based speech recognition can be resource-intensive
5. **Command Scope**: Limited to pre-defined automation capabilities
6. **Context Window**: Limited memory of previous conversation turns
7. **Platform Dependence**: Optimized for Windows, may require adjustments for other platforms

## 🔍 Source Credibility

Jarvis AI employs a multi-layered approach to ensure information credibility:

### Information Sourcing Strategy

- **Smart Classification**: First determines if queries need real-time data or can be answered from knowledge
- **Multi-source Integration**: Gathers information from multiple search results for balanced perspective
- **AI Synthesis**: Uses Groq LLM to intelligently synthesize information from various sources

### Credibility Mechanisms

- **Time Awareness**: Adds current date/time context to every query
- **Source Transparency**: Includes source titles and descriptions in search results
- **Quality Parameters**: Uses advanced search parameters to prioritize reliable sources
- **Three-stage Verification**: Classification → Search → LLM Synthesis pipeline

### Future Enhancements

- Source quality metrics and domain authority scoring
- Cross-reference fact verification across multiple sources
- Formal citation generation for academic/professional use
- User feedback integration for continuous improvement

## 🔝 Competitive Differentiation

Jarvis AI differentiates itself from commercial AI assistants in several key ways:

| Feature | Jarvis AI | Commercial Assistants |
|---------|--------|------------------------|
| Customizability | High (open source) | Limited |
| Privacy | Local processing where possible | Cloud-dependent |
| Platform | Cross-platform potential | Often ecosystem-locked |
| Integration | Flexible with any service | Typically vendor-restricted |
| Cost | Free, API costs only | Often subscription-based |
| Transparency | Full code visibility | Black-box algorithms |

### Key Advantages

1. **First-layer Decision Making**: Unique classification approach before query processing
2. **Hybrid Architecture**: Balance of local functionality and cloud AI
3. **Extensibility**: Easy to add new commands and capabilities
4. **Independence**: Not tied to any specific ecosystem or vendor

## 🔮 Significance and Implications

The development of Jarvis AI has broader implications:

### Technological Impact

- Demonstrates the practical integration of multiple AI services into a cohesive system
- Shows how traditional software can be enhanced with AI capabilities
- Provides a framework for building personalized AI assistants

### Social Implications

- Increases accessibility to AI technology for everyday users
- Raises questions about AI assistants in daily life and human-AI interaction
- Demonstrates the balance between cloud AI power and local control

### Educational Value

- Serves as a learning platform for understanding:
  - Natural language processing
  - Speech recognition systems
  - Multi-threaded application design
  - API integration

## 🛠️ Maintenance and Support Status

### Current Status

Jarvis AI is an actively maintained project with regular updates focused on:

- **Bug fixes**: Addressing issues as they arise
- **Feature enhancements**: Adding new capabilities based on user feedback
- **API updates**: Keeping pace with changes in third-party services

### Support Channels

- **GitHub Issues**: Primary channel for bug reports and feature requests
- **Documentation**: Comprehensive guides for common issues
- **Community Support**: Growing community of contributors

### Update Schedule

- **Major releases**: Quarterly
- **Minor updates**: Monthly
- **Hotfixes**: As needed

## 🔧 Advanced Configuration

You can customize Jarvis by modifying these settings in the `.env` file:

- **Username**: Your name (how you want Jarvis to address you)
- **Assistantname**: The assistant's name (default is "Jarvis")
- **InputLanguage**: Your preferred language for voice input
- **AssistantVoice**: The voice model for speech synthesis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- Inspired by Iron Man's JARVIS
- Built with the power of Groq and Cohere AI
- Special thanks to all the open-source libraries that made this possible

---

<p align="center">Created with ❤️ by Atharva Shinde</p> 
