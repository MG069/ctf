#!/bin/bash
set -e

echo "========================================="
echo "  DarkNet Forum CTF - Setup & Start"
echo "========================================="
echo ""

# Images bauen / pullen
echo "[1/3] Docker Images bauen..."
docker compose build
docker compose pull ollama support
echo "      Done."
echo ""

# Container starten
echo "[2/3] Container starten..."
docker compose up -d
echo "      Done."
echo ""

# Ollama Modell laden
echo "[3/3] tinyllama Modell laden (kann etwas dauern)..."
docker compose exec ollama ollama pull tinyllama
echo "      Done."
echo ""

echo "========================================="
echo "  CTF laeuft! Oeffne im Browser:"
echo "  http://localhost:5000"
echo "========================================="
