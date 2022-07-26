-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS global_tag_map;
DROP TABLE IF EXISTS sce;
DROP TABLE IF EXISTS lifetime;

CREATE TABLE global_tag_map (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  global_tag TEXT UNIQUE NOT NULL,
  sce TEXT NOT NULL,
  lifetime TEXT NOT NULL
);

CREATE TABLE sce (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tag TEXT NOT NULL,
  run_number INTEGER NOT NULL,
  hash TEXT NOT NULL
);

CREATE TABLE lifetime (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tag TEXT NOT NULL,
  run_number INTEGER NOT NULL,
  hash TEXT NOT NULL
);

CREATE TABLE payload (
  hash TEXT NOT NULL,
  payload BLOB NOT NULL
);