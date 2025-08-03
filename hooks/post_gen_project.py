from pathlib import Path
import shutil

def remove(path: Path) -> None:
    """Remove a file or directory if it exists."""
    try:
        if path.is_file():
            path.unlink()
            print(f"Removed file: {path}")
        elif path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
            print(f"Removed directory: {path}")
    except Exception as e:
        print(f" Failed to remove {path}: {e}")

def environment_cleanup(selected_env: str) -> None:
    """
    Removes all environment configuration files and folders 
    that don't match the selected environment.
    """
    root = Path.cwd()

    docker_items = ["Dockerfile", "docker-compose.yaml", ".dockerignore", "docker"]
    conda_file = "environment.yml"
    venv_file = "requirements.txt"

    try:
        if selected_env != "docker":
            for item in docker_items:
                remove(root / item)
        if selected_env != "conda":
            remove(root / conda_file)
        if selected_env != "py_venv":
            remove(root / venv_file)
    except Exception as err:
        print(f" Unexpected cleanup error: {err}")
    finally:
        remove(root / "year.txt")

if __name__ == "__main__":
    environment_cleanup("{{ cookiecutter.environment_manager }}")
