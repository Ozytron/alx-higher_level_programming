-- Script that creates the table on your MySQL server.
-- Query that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256));