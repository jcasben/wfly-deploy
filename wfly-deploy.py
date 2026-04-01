import os
import json
import subprocess
from pathlib import Path
import shutil
import sys

CONFIG_FILE = ".wflydeploy_conf.json"

def get_config():
    if os.path.exists(CONFIG_FILE) and os.path.getsize(CONFIG_FILE) > 0:
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                if "wildfly_path" in config and "group_id" in config:
                    print("✅ Configuración detectada correctamente")
                    return config
        except (json.JSONDecodeError, KeyError):
            print("⚠️ El archivo de configuración está corrupto.")

    print("----- CONFIGURACIÓN INICIAL -----")
    path = input("Introduce la ruta de 'standalone/deployments' de tu Wildfly: ").strip()
    group = input("Introduce tu número de equipo de la práctica (ej: bayes00 -> 00): ").strip()
    path = path.replace('"', '').replace("'", "")

    config = { 
        "wildfly_path": path,
        "group_id": group
    }

    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
    
    return config

def run_maven():
    print("🚀 Compilando proyecto con Maven...")
    result = subprocess.run("mvn clean install", shell=True)
    if result.returncode != 0:
        print("❌ Error en la compilación. Revisa tu código.")
        sys.exit(1)

def deploy(config):
    dir_name = f"bayes{config['group_id']}-ear"
    target_dir = Path(dir_name) / "target"

    print(f"🔍 Buscando el archivo .ear en: {target_dir}")

    ears = list(target_dir.glob("*.ear"))

    if not ears:
        print(f"❌ No se encontró el .ear en {target_dir}")
        return

    ear_file = ears[0]
    dest = config["wildfly_path"]

    try:
        print(f"📦 Desplegando {ear_file.name}...")
        shutil.copy(ear_file, dest)
        print(f"✅ {ear_file.name} desplegado en {dest}")
    except Exception as e:
        print(f"Se produjo un error copiando el .ear a Wildfly: {e}")

if __name__ == "__main__":
    conf = get_config()
    run_maven()
    deploy(conf)