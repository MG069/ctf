# DarkNet Forum CTF

## Voraussetzungen

- Docker + Docker Compose
- Linux / WSL (Windows Subsystem for Linux)
- Internetzugang (fuer Ollama + MySQL Image Pull)

## Schnellstart

```bash
chmod +x start_ctf.sh
./start_ctf.sh
```

Danach ist das Forum unter **http://localhost:5000** erreichbar.

## Manueller Start

```bash
docker compose build
docker compose up -d
docker compose exec ollama ollama pull tinyllama
```

## Stoppen

```bash
docker compose down
```

## Reset (Datenbank zuruecksetzen)

```bash
docker compose down -v
docker compose up -d
docker compose exec ollama ollama pull tinyllama
```
