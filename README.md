# developing-the-interactive-web-lec-3-ameliavrieze

make venv: uv venv
activate venv: .venv/Scripts/activate
add dependency: uv add
sync: uv sync

flask --app developing_the_interactive_web_lec_3_ameliavrieze.server run 