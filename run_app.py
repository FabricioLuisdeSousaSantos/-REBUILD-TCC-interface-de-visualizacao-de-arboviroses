import os
import sys
from streamlit.web import cli as stcli

def resource_path(rel_path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel_path)

if __name__ == "__main__":
    sys.argv = [
        "streamlit", "run", resource_path("sistema_de_avaliacao.py"),
        "--global.developmentMode=false",
        "--browser.gatherUsageStats=false",
    ]
    sys.exit(stcli.main())