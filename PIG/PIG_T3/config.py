import os
import sys
import json

# Константа расширений
EXTENSION_TO_MARKDOWN = {
    '.cs': 'csharp', '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
    '.html': 'html', '.css': 'css', '.json': 'json', '.xml': 'xml', '.xaml': 'xml',
    '.cpp': 'cpp', '.c': 'c', '.h': 'cpp', '.java': 'java', '.sql': 'sql',
    '.sh': 'bash', '.bat': 'batch', '.txt': 'text', '.md': 'markdown',
    '.vue': 'javascript', '.jsx': 'javascript', '.tsx': 'typescript',
    '.go': 'go', '.rs': 'rust', '.php': 'php', '.rb': 'ruby'
}

class ConfigManager:
    def __init__(self):
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.config_file = os.path.join(base_dir, "app_config.json")
        self.default_config = {
            "root_folder": base_dir,
            "extensions": ".py, .yml, .txt, .example",
            "ignore_list": "PIG_T3, .git, .vs, .idea, __pycache__, venv, node_modules, .lock, obj, bin, build, dist, .vscode, log.txt, auto_migration_at_startup.py, project_context.txt, database, WORK_TIME, debug",
            "output_name": "project_context",
            "include_empty_folders": False,
            "strict_mode": False,
            "ignore_self": False,
            "add_edit_prompt": False,
            "auto_copy_file": False,
            "line_numbers": False,
            "use_sharp_indent": False,
            "ollama_model": "None",
            "ollama_options": {
                "num_ctx": 24000,
                "num_predict": 12000,
                "temperature": 0.5,
                "top_p": 0.95,
                "top_k": 100
            },
            "opt_chunk_size": 7000,
            "opt_chunk_unit": "tokens",
            "opt_default_model": "None",
            "ui_tree_expanded": [],
            "ui_tree_unchecked": [],
            "theme": "dark",
            "font_size": 10,
            "tree_row_height": 28,
            "checkbox_size": 14,
            "tabs_visibility": {
                "generator": True,
                "info": True,
                "editor": True,
                "quality": True
            }
        }

    def load(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return {**self.default_config, **json.load(f)}
            except Exception:
                return self.default_config
        return self.default_config

    def save(self, data):
        try:
            json_str = json.dumps(data, indent=4, ensure_ascii=False)
            with open(self.config_file, 'w', encoding='utf-8') as f:
                f.write(json_str)
        except Exception as e:
            print(f"Не удалось сохранить настройки: {e}")
