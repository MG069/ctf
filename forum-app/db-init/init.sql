-- =============================================
-- Forum Backup Database
-- Last updated: 2026-03-20
-- WARNUNG: Diese DB enthält sensible Daten!
-- =============================================

USE forum_backup;

CREATE TABLE user_credentials (
    id INT PRIMARY KEY,
    username VARCHAR(100),
    password_hash VARCHAR(255) COMMENT 'MD5',
    role VARCHAR(50),
    email VARCHAR(255),
    last_login DATETIME
);

INSERT INTO user_credentials VALUES
(1, 'r00t_overlord', '**REDACTED**', 'root', 'root@darknet-forum.local', '2026-03-25 23:59:59'),
(2, 'admin', '5aca695374f4ee2032155a565ad78462', 'admin', 'admin@darknet-forum.local', '2026-03-26 14:22:10'),
(3, 'sh4d0w_mod', '9a2a0c57712edc937b4e3a2e78923c4e', 'moderator', 'shadow@darknet-forum.local', '2026-03-26 09:15:33'),
(4, 'cyberph4ntom', 'e2fc714c4727ee9395f324cd2e7f331f', 'vip', 'phantom@darknet-forum.local', '2026-03-24 18:45:00'),
(5, 'n00b_hacker', '3c59dc048e8850243be8079a5c74d079', 'member', 'noob@darknet-forum.local', '2026-03-20 11:30:00'),
(6, 'darkbyte', 'a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6', 'member', 'dark@darknet-forum.local', '2026-03-22 16:00:00'),
(7, 'guest', 'e99a18c428cb38d5f260853678922e03', 'guest', 'guest@darknet-forum.local', '2026-03-26 10:00:00');

-- Admin password hash: 5aca695374f4ee2032155a565ad78462 = MD5(r00tk1t)
-- Use https://crackstation.net to crack
