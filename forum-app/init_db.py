"""
Initialisiert die SQLite-Datenbank mit allen CTF-Usern und Forum-Posts.
"""
import sqlite3
import hashlib
import base64
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "forum.db")


def md5_hash(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def init():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # ── Users ──────────────────────────────────────────────
    c.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'guest',
            bio TEXT DEFAULT '',
            avatar TEXT DEFAULT '👤'
        )
    """)

    users = [
        # id=1  root (hidden, final goal)
        ("r00t_overlord", md5_hash("R00T{m4st3r_h4ck3r}"), "root",
         "I am the one above all.", "👑"),
        # id=2  admin (C6 target – password: r00tk1t)
        ("admin", md5_hash("r00tk1t"), "admin",
         "Forum administrator. Do not disturb.", "⚙️"),
        # id=3  moderator (C5 – careless note in bio)
        ("sh4d0w_mod", md5_hash("m0dP4ss!"), "moderator",
         "📝 TODO: Forum-Backup-DB updaten!", "🛡️"),
        # id=4  vip user
        ("cyberph4ntom", md5_hash("ph4nt0m"), "vip",
         "d2FydW13YW5kZWxzdGR1ZGVua2V5dW0/",
         "👻"),
        # id=5  regular user
        ("n00b_hacker", md5_hash("hacker123"), "member",
         "Ich bin neu hier und will alles lernen!", "🐣"),
        # id=6  regular user
        ("darkbyte", md5_hash("darkbyte99"), "member",
         "0xDEADBEEF is my favorite constant.", "🖥️"),
        # id=7  guest (C1 login – discoverable in source)
        ("guest", md5_hash("W3lc0me!"), "guest",
         "Just browsing...", "👋"),
    ]

    c.executemany(
        "INSERT INTO users (username, password, role, bio, avatar) VALUES (?,?,?,?,?)",
        users,
    )

    # ── Forum Posts ────────────────────────────────────────
    c.execute("""
        CREATE TABLE posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT DEFAULT 'general',
            pinned INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    posts = [
        # Honeypot post (pinned, looks legit)
        (2, "🔒 Exploit-Sammlung v3.2 – Download verfügbar",
         "Die neue Exploit-Sammlung ist online. Zugang nur für verifizierte Members. "
         '<a href="/honeypot" class="btn btn-sm btn-hacker">📥 Zum Download-Bereich</a>',
         "announcements", 1),

        # Normal posts
        (5, "Wie fange ich mit Hacking an?",
         "Hey Leute, ich bin total neu hier. Kann mir jemand Tipps geben?",
         "general", 0),

        (6, "0xDEADBEEF – Die beste Hex-Konstante",
         "Wer kennt sie nicht? Ich benutze sie überall in meinem Code. "
         "Fun Fact: Sie wird seit den 80ern als Debug-Marker verwendet.",
         "general", 0),

        (4, "Neues Kali Linux Release",
         "Hat jemand schon Kali 2026.1 getestet? Die neuen Tools "
         "im Wireless-Bereich sehen vielversprechend aus.",
         "general", 0),

        (3, "Server-Hardening Checkliste",
         "Bin gerade dabei unsere internen Server abzusichern. "
         "Wer von euch hat Erfahrung mit MySQL-Hardening? "
         "Hab das Gefühl da läuft noch einiges mit Default-Configs...",
         "general", 0),

        (6, "CTF Writeup: HackTheBox - Keeper",
         "Geiler Kasten! Root war über nen KeePass memory dump möglich. "
         "Wer Hilfe braucht kann mich anschreiben.",
         "general", 0),

        (5, "Suche Lernpartner für OSCP",
         "Will nächstes Semester OSCP machen. Jemand Bock "
         "zusammen zu lernen? TryHackMe und HackTheBox hab ich schon durch.",
         "general", 0),
    ]

    c.executemany(
        "INSERT INTO posts (user_id, title, content, category, pinned) VALUES (?,?,?,?,?)",
        posts,
    )

    conn.commit()
    conn.close()
    print(f"[✓] Datenbank initialisiert: {DB_PATH}")
    print(f"[✓] Admin-Hash (r00tk1t): {md5_hash('r00tk1t')}")
    print(f"[✓] {len(users)} User angelegt")
    print(f"[✓] {len(posts)} Posts angelegt")


if __name__ == "__main__":
    init()
