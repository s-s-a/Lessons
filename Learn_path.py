# https://vkvideo.ru/video-225894706_456239107
from pathlib import Path

# лучше использовать Path, а не os.path или сырые пути в стиле r'С://folder!
# удобно читать и писать текст/байты, если нужно сразу все прочитать/записать
# лучше всегда указывать кодировку UTF-&
# для получения полного пути, имени, расширения используем атрибуты, а не строки

content = Path("one.txt").read_text(encoding="utf-8")
content = f"{content}\n22222"
Path("two.txt").write_text(content, encoding="utf-8")


script_path = Path(__file__)

print(script_path)
print(script_path.parent)
print(script_path.name)
print(script_path.stem)
print(script_path.suffix)
print(script_path.parts)
print(script_path.is_dir())
print(script_path.is_file())
print(script_path.exists())
print(script_path.stat())


DATA_DIR = script_path.parent / 'data'
DATA_FILE = DATA_DIR / 'some_data.txt'

if DATA_FILE.exists():
    content = DATA_FILE.read_text(encoding='utf-8')
    print(content)

LOGS_DIR = script_path.parent / 'Logs'
LOG_FILE = LOGS_DIR / 'main. Log'

if not LOGS_DIR.exists():
    LOGS_DIR.mkdir()
if not LOG_FILE.exists():
    LOG_FILE.touch()
    LOG_FILE.write_text("Start", 'utf-8')


PATHS = script_path.parent

for path in PATHS.iterdir():
    if path.is_dir():
        print(f"Folder name {path. name}")
    elif path.is_file() and path.suffix == '.txt':
        print(f"File name {path.name}, size {path.stat().st_size}")

for path in PATHS.glob("*.txt"):
    print(f"File name {path.name}, size {path.stat().st_size}")

for path in PATHS.glob("**/*.txt"):
    print(f"File name {path.name}, size {path.stat().st_size}")
