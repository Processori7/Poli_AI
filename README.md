# Pollinations AI Agent 🤖🎨

Многофункциональный AI-агент для работы с Pollinations.ai API. Поддерживает генерацию изображений, аудио, работу с файлами, интернет-поиск и многое другое!

## 🚀 Возможности

### 🎨 Генерация контента
- **Изображения**: Генерация изображений с выбором модели (flux, turbo, kontext, gptimage)
- **Аудио**: Text-to-Speech с 6 голосами (alloy, echo, fable, onyx, nova, shimmer) 🎵
- **Текст**: Общение с различными AI моделями

### 📁 Файловая система
- Создание, чтение, запись, удаление файлов
- Управление папками
- Перемещение и переименование файлов

### 🌐 Интернет и загрузки
- Поиск в интернете (SearchGPT, ElixpoSearch)
- Загрузка файлов и изображений
- Поиск и загрузка изображений

### 💻 Разработка
- Выполнение системных команд
- Запуск Python кода
- Создание Python проектов с виртуальным окружением
- Автоматическая разработка ПО с исправлением ошибок

### ⚙️ Системное управление
- Получение информации о системе
- Управление службами Windows
- Изменение реестра Windows

## 📋 Требования

- Python 3.8+
- Windows/Linux/macOS
- Интернет-соединение

## 🛠️ Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Processori7/Poli_AI.git
   cd Poli_AI
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройте API токен (опционально для аудио):**
   
   Создайте файл `.env` в корневой папке:
   ```env
   # Получите токен на https://auth.pollinations.ai/
   POLLINATIONS_TOKEN=ваш_токен_здесь
   DEFAULT_MODEL=openai
   MAX_ATTEMPTS=3
   INTERFACE_LANGUAGE=ru  # Язык интерфейса по умолчанию
   OUTPUT_LANGUAGE=ru    # Язык вывода по умолчанию
   FIRST_STARTUP_LANGUAGE_SELECTION=true  # Показать выбор языка при первом запуске
   ```

   **Для генерации аудио токен обязателен!** 🔑

## 🎯 Запуск

```bash
python main.py
```

### 🎛️ Первоначальная настройка

1. Выберите модель AI из списка доступных или используйте модель по умолчанию
2. Выберите язык интерфейса и вывода при первом запуске (если включено)
3. Введите задачу на естественном языке
4. Агент автоматически выполнит задачу или предложит план

## 📝 Примеры использования

### 🎨 Генерация изображений
```
Сгенерируй изображение красивого заката над океаном
```

### 🎵 Генерация аудио (требует токен)
```
Сгенерируй аудио с текстом "Привет, мир!"
```

### 📁 Работа с файлами
```
Создай папку "Проекты" и файл "README.md" в ней
```

### 🌐 Поиск в интернете
```
Найди последние новости о искусственном интеллекте
```

### 💻 Разработка
```
Создай Python программу для подсчета факториала
```

## 🔑 API Токены

### Получение токена

1. Перейдите на [auth.pollinations.ai](https://auth.pollinations.ai/)
2. Зарегистрируйтесь или войдите в аккаунт
3. Получите API токен
4. Добавьте его в `.env` файл

### Для чего нужен токен?

- **Обязательно**: Генерация аудио 🎵
- **Опционально**: Генерация изображений и текста (повышает приоритет и убирает ограничения)

### Без токена доступно:
- ✅ Генерация изображений (с ограничениями)
- ✅ Текстовое общение с AI
- ✅ Все функции файловой системы
- ✅ Интернет-поиск и загрузки
- ❌ Генерация аудио

## 🎨 Доступные модели

### Текстовые модели
- **OpenAI GPT-4.1** - Универсальная модель
- **DeepSeek V3** - Продвинутая модель рассуждений
- **Grok-3 Mini** - Быстрая модель от xAI
- **Mistral Small** - Эффективная европейская модель
- **SearchGPT** - Специализированная модель для поиска
- И многие другие...

### Модели изображений
- **Flux** - Высокое качество (по умолчанию)
- **Turbo** - Быстрая генерация
- **Kontext** - Специализированная модель
- **GPTImage** - От OpenAI

### Голоса для аудио
- **Alloy** - Нейтральный голос
- **Echo** - Четкий и ясный
- **Fable** - Выразительный
- **Onyx** - Глубокий голос
- **Nova** - Женский голос
- **Shimmer** - Мягкий и теплый

## 📂 Структура проекта

```
Poli_AI/
├── main.py              # Основной файл агента
├── requirements.txt     # Зависимости Python
├── .env                 # API токены (создайте сами)
├── README.md           # Документация
├── output/             # Папка для сгенерированных файлов
│   ├── images/         # Изображения
│   └── audio/          # Аудио файлы
└── pollinations_agent.log # Логи работы
```

## 🛡️ Безопасность

- Агент запрашивает подтверждение для потенциально опасных операций
- Системные команды требуют явного разрешения
- API токены должны храниться в `.env` файле (не в коде!)
- Все запросы к API помечены как `private=true`

## 🐛 Устранение неполадок

### Проблемы с аудио
- Убедитесь, что в `.env` файле указан корректный токен
- Проверьте интернет-соединение
- Токен должен иметь права на генерацию аудио

### Проблемы с изображениями
- Проверьте интернет-соединение
- Попробуйте другую модель генерации
- Добавьте токен для повышения приоритета

### Ошибки файловой системы
- Проверьте права доступа к папкам
- Убедитесь в корректности путей
- На Windows может потребоваться запуск от администратора

## 📄 Лицензия

MIT License - см. файл LICENSE для деталей.

## 🤝 Вклад в проект

Приветствуются Pull Request'ы и предложения по улучшению!

## 📞 Поддержка

Если у вас возникли вопросы:
1. Проверьте этот README
2. Посмотрите логи в `pollinations_agent.log`
3. Создайте Issue в репозитории

---

---

# English Documentation

# Pollinations AI Agent 🤖🎨

Multifunctional AI agent for working with Pollinations.ai API. Supports image generation, audio, file management, internet search and much more!

## 🚀 Features

### 🎨 Content Generation
- **Images**: Image generation with model selection (flux, turbo, kontext, gptimage)
- **Audio**: Text-to-Speech with 6 voices (alloy, echo, fable, onyx, nova, shimmer) 🎵
- **Text**: Chat with various AI models

### 📁 File System
- Create, read, write, delete files
- Folder management
- Move and rename files

### 🌐 Internet and Downloads
- Internet search (SearchGPT, ElixpoSearch)
- File and image downloads
- Image search and download

### 💻 Development
- Execute system commands
- Run Python code
- Create Python projects with virtual environments
- Automatic software development with error correction

### ⚙️ System Management
- Get system information
- Manage Windows services
- Modify Windows registry

## 📋 Requirements

- Python 3.8+
- Windows/Linux/macOS
- Internet connection

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Poli_AI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API token (optional for audio):**
   
   Create a `.env` file in the root folder:
   ```env
   # Get token at https://auth.pollinations.ai/
   POLLINATIONS_TOKEN=your_token_here
   DEFAULT_MODEL=openai
   MAX_ATTEMPTS=3
   INTERFACE_LANGUAGE=en  # Default interface language
   OUTPUT_LANGUAGE=en    # Default output language
   FIRST_STARTUP_LANGUAGE_SELECTION=true  # Show language selection on first startup
   ```

   **Token is required for audio generation!** 🔑

## 🎯 Usage

```bash
python main.py
```

### 🎛️ Initial Setup

1. Select AI model from available list or use default model
2. Choose interface and output language on first startup (if enabled)
3. Enter task in natural language
4. Agent will automatically execute task or suggest a plan

## 📝 Usage Examples

### 🎨 Image Generation
```
Generate an image of a beautiful sunset over the ocean
```

### 🎵 Audio Generation (requires token)
```
Generate audio with text "Hello, world!"
```

### 📁 File Operations
```
Create a "Projects" folder and "README.md" file in it
```

### 🌐 Internet Search
```
Find latest news about artificial intelligence
```

### 💻 Development
```
Create a Python program to calculate factorial
```

## 🔑 Configuration Options

### Environment Variables (.env file)

| Variable | Default | Description |
|----------|---------|-------------|
| `POLLINATIONS_TOKEN` | - | API token for enhanced features |
| `DEFAULT_MODEL` | openai | Default AI model to use |
| `MAX_ATTEMPTS` | 3 | Maximum attempts for task execution |
| `INTERFACE_LANGUAGE` | ru | Interface language (ru/en) |
| `OUTPUT_LANGUAGE` | ru | AI response language (ru/en) |
| `FIRST_STARTUP_LANGUAGE_SELECTION` | true | Show language selection on first run |
| `DEFAULT_VOICE` | alloy | Default TTS voice |
| `REQUIRE_CONFIRMATION` | true | Require confirmation for dangerous operations |
| `DEBUG_MODE` | false | Enable debug information |

### Language Support

The agent supports both Russian and English:
- **Interface Language**: Controls menu text and prompts
- **Output Language**: Controls AI response language
- **First Startup Selection**: Interactive language setup on first run

### Model Selection

You can set a default model or choose interactively:
- Available models are fetched from Pollinations API
- Models include OpenAI GPT, DeepSeek, Grok, Mistral, and more
- Model can be changed during runtime with 'change' command

### Retry Logic

The agent automatically retries failed tasks:
- `MAX_ATTEMPTS` controls the number of retry attempts
- Intelligent error analysis and code correction
- Progressive problem-solving approach

## 🛡️ Security Features

- Confirmation prompts for dangerous operations
- System commands require explicit permission
- API tokens stored securely in `.env` file
- All API requests marked as `private=true`
- Registry and service operations require confirmation

## 🎨 Available Models

### Text Models
- **OpenAI GPT-4.1** - Universal model
- **DeepSeek V3** - Advanced reasoning model
- **Grok-3 Mini** - Fast model by xAI
- **Mistral Small** - Efficient European model
- **SearchGPT** - Specialized search model
- And many others...

### Image Models
- **Flux** - High quality (default)
- **Turbo** - Fast generation
- **Kontext** - Specialized model
- **GPTImage** - By OpenAI

### Audio Voices
- **Alloy** - Neutral voice
- **Echo** - Clear and crisp
- **Fable** - Expressive
- **Onyx** - Deep voice
- **Nova** - Female voice
- **Shimmer** - Soft and warm

## 🐛 Troubleshooting

### Audio Issues
- Ensure correct token in `.env` file
- Check internet connection
- Token must have audio generation permissions

### Image Issues
- Check internet connection
- Try different generation model
- Add token for higher priority

### File System Errors
- Check folder permissions
- Verify path correctness
- May require administrator rights on Windows

### Language Issues
- Delete `.env` file to reset language selection
- Set `FIRST_STARTUP_LANGUAGE_SELECTION=true` to show language menu
- Manually edit language settings in `.env` file

## 📄 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

Pull requests and suggestions for improvements are welcome!

## 📞 Support

If you have questions:
1. Check this README
2. Look at logs in `pollinations_agent.log`
3. Create an Issue in the repository

---
