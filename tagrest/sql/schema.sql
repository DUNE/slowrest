-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS global_tag_map;
DROP TABLE IF EXISTS hash_map;
DROP TABLE IF EXISTS sce;
DROP TABLE IF EXISTS lifetime;
DROP TABLE IF EXISTS payload;


CREATE TABLE global_tag_map (
  --id INTEGER PRIMARY KEY AUTOINCREMENT,
  global_tag TEXT UNIQUE NOT NULL,
  sce TEXT NOT NULL,
  lifetime TEXT NOT NULL
);

CREATE TABLE global_tag_map_new (
  --id INTEGER PRIMARY KEY AUTOINCREMENT,
  global_tag TEXT NOT NULL,
  kind TEXT NOT NULL,
  tag TEXT NOT NULL
);

CREATE TABLE hash_map (
  --id INTEGER PRIMARY KEY AUTOINCREMENT,
  kind TEXT NOT NULL,
  tag TEXT NOT NULL,
  run_number INTEGER NOT NULL,
  hash TEXT NOT NULL
);

CREATE TABLE sce (
  --id INTEGER PRIMARY KEY AUTOINCREMENT,
  tag TEXT NOT NULL,
  run_number INTEGER NOT NULL,
  hash TEXT NOT NULL
);

CREATE TABLE lifetime (
  --id INTEGER PRIMARY KEY AUTOINCREMENT,
  tag TEXT NOT NULL,
  run_number INTEGER NOT NULL,
  hash TEXT NOT NULL
);

CREATE TABLE payload (
  --id INTEGER PRIMARY KEY AUTOINCREMENT,
  hash TEXT NOT NULL,
  payload BLOB NOT NULL
);

