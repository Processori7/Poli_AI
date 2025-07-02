# -*- coding: utf-8 -*-
"""
Модуль интернационализации для Pollinations AI Agent
Поддержка русского и английского языков
"""

# Словари переводов
TRANSLATIONS = {
    'ru': {
        # Основные сообщения
        'welcome': 'Добро пожаловать в Pollinations AI Agent! 🤖🎨',
        'agent_started': 'Pollinations AI Agent запущен!',
        'agent_stopped': 'До свидания! 👋',
        'task_processing': 'Обработка задачи...',
        'task_completed': 'Задача выполнена успешно!',
        'task_failed': 'Задача не выполнена',
        'error': 'Ошибка',
        'success': 'Успешно',
        'warning': 'Предупреждение',
        
        # Управление моделями
        'available_models': 'Доступные модели:',
        'select_model': 'Выберите модель по номеру:',
        'invalid_choice': 'Неверный выбор, используется стандартная модель.',
        'model_selected': 'Выбрана модель:',
        'change_model': 'Смена модели',
        
        # Интерфейс
        'enter_task': 'Введите вашу задачу (или \'exit\' для выхода, \'change\' для смены модели):',
        'enter_task_short': 'Введите вашу задачу:',
        'exit_command': 'exit',
        'change_command': 'change',
        'result': 'Результат:',
        'yes': 'да',
        'no': 'нет',
        'continue': 'продолжить',
        'skip': 'пропустить',
        
        # API и токены
        'api_token_loaded': 'API токен загружен',
        'api_token_missing': 'API токен не найден',
        'api_token_required': 'Для этой функции требуется API токен',
        'get_token_instruction': 'Получите токен на: https://auth.pollinations.ai/',
        'add_token_instruction': 'Добавьте токен в .env файл: POLLINATIONS_TOKEN=ваш_токен',
        
        # Генерация контента
        'generating_image': 'Генерация изображения...',
        'generating_audio': 'Генерация аудио...',
        'image_generated': 'Изображение сгенерировано:',
        'audio_generated': 'Аудио сгенерировано:',
        'prompt': 'Промпт:',
        'size': 'Размер:',
        'model': 'Модель:',
        'voice': 'Голос:',
        
        # Файловая система
        'file_created': 'Файл создан:',
        'file_read': 'Файл прочитан:',
        'file_written': 'Файл записан:',
        'file_deleted': 'Файл удален:',
        'file_moved': 'Файл перемещен:',
        'directory_created': 'Папка создана:',
        'directory_deleted': 'Папка удалена:',
        'directory_scanned': 'Директория просканирована:',
        
        # Ошибки файловой системы
        'file_not_found': 'Файл не найден:',
        'directory_not_found': 'Папка не найдена:',
        'permission_denied': 'Доступ запрещен:',
        'file_exists': 'Файл уже существует:',
        'directory_exists': 'Папка уже существует:',
        
        # Интернет и загрузки
        'downloading': 'Загрузка...',
        'downloaded': 'Загружено:',
        'searching': 'Поиск...',
        'search_completed': 'Поиск завершен',
        'download_error': 'Ошибка загрузки:',
        'search_error': 'Ошибка поиска:',
        
        # Системные операции
        'executing_command': 'Выполняется команда:',
        'command_executed': 'Команда выполнена',
        'command_failed': 'Команда не выполнена',
        'python_code_executed': 'Python код выполнен',
        'system_info': 'Информация о системе',
        
        # Подтверждения
        'confirm_command': 'Разрешить выполнение команды?',
        'confirm_python': 'Разрешить выполнение Python кода?',
        'confirm_registry': 'Разрешить изменение реестра?',
        'confirm_service': 'Разрешить управление службой?',
        'operation_cancelled': 'Операция отменена пользователем',
        
        # Голоса
        'available_voices': 'Доступные голоса:',
        'select_voice': 'Выберите голос или нажмите Enter для',
        'current_voice': '(текущий)',
        'voice_selected': 'Выбран голос:',
        'default_voice': 'Используется голос по умолчанию:',
        
        # Модели изображений
        'available_image_models': 'Доступные модели изображений:',
        'select_image_model': 'Выберите модель или нажмите Enter для',
        'current_model': '(текущая)',
        'model_selected_img': 'Выбрана модель:',
        'default_model': 'Используется модель по умолчанию:',
        
        # Попытки и повторы
        'attempt': 'Попытка',
        'max_attempts': 'Максимальное количество попыток:',
        'retry': 'Повторная попытка...',
        'failed_after_attempts': 'Не удалось выполнить после попыток:',
        
        # Языки
        'language_selection': 'Выбор языка / Language Selection',
        'select_interface_language': 'Выберите язык интерфейса:',
        'select_output_language': 'Выберите язык ответов AI:',
        'russian': 'Русский',
        'english': 'English',
        'language_saved': 'Настройки языка сохранены',
        'restart_required': 'Перезапустите программу для применения изменений',
        
        # Настройки
        'settings': 'Настройки',
        'current_settings': 'Текущие настройки:',
        'change_settings': 'Изменить настройки',
        'settings_saved': 'Настройки сохранены',
        'settings_file': 'Файл настроек:',
        
        # Отладка
        'debug_mode': 'Режим отладки',
        'debug_info': 'Отладочная информация:',
        'received_data': 'Получены данные:',
        'sending_request': 'Отправка запроса...',
        'response_received': 'Ответ получен',
    },
    
    'en': {
        # Basic messages
        'welcome': 'Welcome to Pollinations AI Agent! 🤖🎨',
        'agent_started': 'Pollinations AI Agent started!',
        'agent_stopped': 'Goodbye! 👋',
        'task_processing': 'Processing task...',
        'task_completed': 'Task completed successfully!',
        'task_failed': 'Task failed',
        'error': 'Error',
        'success': 'Success',
        'warning': 'Warning',
        
        # Model management
        'available_models': 'Available models:',
        'select_model': 'Select model by number:',
        'invalid_choice': 'Invalid choice, using default model.',
        'model_selected': 'Selected model:',
        'change_model': 'Change model',
        
        # Interface
        'enter_task': 'Enter your task (or \'exit\' to quit, \'change\' to change model):',
        'enter_task_short': 'Enter your task:',
        'exit_command': 'exit',
        'change_command': 'change',
        'result': 'Result:',
        'yes': 'yes',
        'no': 'no',
        'continue': 'continue',
        'skip': 'skip',
        
        # API and tokens
        'api_token_loaded': 'API token loaded',
        'api_token_missing': 'API token not found',
        'api_token_required': 'API token required for this function',
        'get_token_instruction': 'Get token at: https://auth.pollinations.ai/',
        'add_token_instruction': 'Add token to .env file: POLLINATIONS_TOKEN=your_token',
        
        # Content generation
        'generating_image': 'Generating image...',
        'generating_audio': 'Generating audio...',
        'image_generated': 'Image generated:',
        'audio_generated': 'Audio generated:',
        'prompt': 'Prompt:',
        'size': 'Size:',
        'model': 'Model:',
        'voice': 'Voice:',
        
        # File system
        'file_created': 'File created:',
        'file_read': 'File read:',
        'file_written': 'File written:',
        'file_deleted': 'File deleted:',
        'file_moved': 'File moved:',
        'directory_created': 'Directory created:',
        'directory_deleted': 'Directory deleted:',
        'directory_scanned': 'Directory scanned:',
        
        # File system errors
        'file_not_found': 'File not found:',
        'directory_not_found': 'Directory not found:',
        'permission_denied': 'Permission denied:',
        'file_exists': 'File already exists:',
        'directory_exists': 'Directory already exists:',
        
        # Internet and downloads
        'downloading': 'Downloading...',
        'downloaded': 'Downloaded:',
        'searching': 'Searching...',
        'search_completed': 'Search completed',
        'download_error': 'Download error:',
        'search_error': 'Search error:',
        
        # System operations
        'executing_command': 'Executing command:',
        'command_executed': 'Command executed',
        'command_failed': 'Command failed',
        'python_code_executed': 'Python code executed',
        'system_info': 'System information',
        
        # Confirmations
        'confirm_command': 'Allow command execution?',
        'confirm_python': 'Allow Python code execution?',
        'confirm_registry': 'Allow registry modification?',
        'confirm_service': 'Allow service management?',
        'operation_cancelled': 'Operation cancelled by user',
        
        # Voices
        'available_voices': 'Available voices:',
        'select_voice': 'Select voice or press Enter for',
        'current_voice': '(current)',
        'voice_selected': 'Selected voice:',
        'default_voice': 'Using default voice:',
        
        # Image models
        'available_image_models': 'Available image models:',
        'select_image_model': 'Select model or press Enter for',
        'current_model': '(current)',
        'model_selected_img': 'Selected model:',
        'default_model': 'Using default model:',
        
        # Attempts and retries
        'attempt': 'Attempt',
        'max_attempts': 'Maximum attempts:',
        'retry': 'Retrying...',
        'failed_after_attempts': 'Failed after attempts:',
        
        # Languages
        'language_selection': 'Language Selection / Выбор языка',
        'select_interface_language': 'Select interface language:',
        'select_output_language': 'Select AI response language:',
        'russian': 'Русский',
        'english': 'English',
        'language_saved': 'Language settings saved',
        'restart_required': 'Restart the program to apply changes',
        
        # Settings
        'settings': 'Settings',
        'current_settings': 'Current settings:',
        'change_settings': 'Change settings',
        'settings_saved': 'Settings saved',
        'settings_file': 'Settings file:',
        
        # Debug
        'debug_mode': 'Debug mode',
        'debug_info': 'Debug information:',
        'received_data': 'Received data:',
        'sending_request': 'Sending request...',
        'response_received': 'Response received',
    }
}

def get_text(key, language='ru', **kwargs):
    """
    Получает переведенный текст по ключу
    
    Args:
        key (str): Ключ текста
        language (str): Язык ('ru' или 'en')
        **kwargs: Дополнительные параметры для форматирования
    
    Returns:
        str: Переведенный текст
    """
    if language not in TRANSLATIONS:
        language = 'ru'  # Fallback к русскому
    
    text = TRANSLATIONS[language].get(key, key)
    
    # Форматирование строки если переданы параметры
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, ValueError):
            pass  # Если форматирование не удалось, возвращаем как есть
    
    return text

def get_language_settings():
    """
    Возвращает настройки языка из переменных окружения
    
    Returns:
        dict: Словарь с настройками языка
    """
    import os
    return {
        'interface': os.getenv('INTERFACE_LANGUAGE', 'ru'),
        'output': os.getenv('OUTPUT_LANGUAGE', 'ru'),
        'first_startup': os.getenv('FIRST_STARTUP_LANGUAGE_SELECTION', 'true').lower() == 'true'
    }

def save_language_settings(interface_lang, output_lang):
    """
    Сохраняет настройки языка в .env файл
    
    Args:
        interface_lang (str): Язык интерфейса
        output_lang (str): Язык вывода
    """
    import os
    from dotenv import set_key
    
    env_file = '.env'
    
    # Сохраняем настройки
    set_key(env_file, 'INTERFACE_LANGUAGE', interface_lang)
    set_key(env_file, 'OUTPUT_LANGUAGE', output_lang)
    set_key(env_file, 'FIRST_STARTUP_LANGUAGE_SELECTION', 'false')

def show_language_selection():
    """
    Показывает диалог выбора языка при первом запуске
    
    Returns:
        tuple: (interface_language, output_language)
    """
    print("=" * 50)
    print("🌍 Language Selection / Выбор языка")
    print("=" * 50)
    
    # Выбор языка интерфейса
    print("\n1. Select interface language / Выберите язык интерфейса:")
    print("   1) Русский (Russian)")
    print("   2) English")
    
    while True:
        try:
            choice = input("\nYour choice / Ваш выбор (1-2): ").strip()
            if choice == '1':
                interface_lang = 'ru'
                break
            elif choice == '2':
                interface_lang = 'en'
                break
            else:
                print("❌ Invalid choice / Неверный выбор. Please select 1 or 2 / Выберите 1 или 2")
        except (ValueError, KeyboardInterrupt):
            interface_lang = 'ru'  # По умолчанию русский
            break
    
    # Используем выбранный язык для дальнейших сообщений
    print(f"\n✅ {get_text('language_saved', interface_lang)}")
    
    # Выбор языка ответов AI
    print(f"\n2. {get_text('select_output_language', interface_lang)}")
    print(f"   1) {get_text('russian', interface_lang)}")
    print(f"   2) {get_text('english', interface_lang)}")
    
    while True:
        try:
            choice = input(f"\n{get_text('select_voice', interface_lang)} (1-2): ").strip()
            if choice == '1':
                output_lang = 'ru'
                break
            elif choice == '2':
                output_lang = 'en'
                break
            else:
                print(f"❌ {get_text('invalid_choice', interface_lang)}")
        except (ValueError, KeyboardInterrupt):
            output_lang = interface_lang  # По умолчанию как интерфейс
            break
    
    print(f"\n✅ {get_text('settings_saved', interface_lang)}")
    print("=" * 50)
    
    return interface_lang, output_lang

# Функция для перевода промптов в запросах к AI
def translate_prompt_for_ai(prompt, target_language='en'):
    """
    Переводит промпт для AI на указанный язык (если требуется)
    
    Args:
        prompt (str): Исходный промпт
        target_language (str): Целевой язык
    
    Returns:
        str: Переведенный или исходный промпт
    """
    if target_language == 'en':
        # Добавляем инструкцию отвечать на английском
        return f"Answer in English. {prompt}"
    elif target_language == 'ru':
        # Добавляем инструкцию отвечать на русском
        return f"Отвечай на русском языке. {prompt}"
    else:
        return prompt
