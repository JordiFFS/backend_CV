#!/bin/bash

# Obtener la ruta completa del script
SCRIPT_PATH="$(realpath "${BASH_SOURCE[0]}")"
echo "La ruta completa del script es: $SCRIPT_PATH"

# Obtener solo el directorio
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"
cd $SCRIPT_DIR||exit

source $SCRIPT_DIR/env/bin/activate

# Ejecutar Daphne
exec daphne -b 0.0.0.0 -p 8001 DJcv_backend.asgi:application