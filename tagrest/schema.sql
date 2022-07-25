-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS global_tag_map;
DROP TABLE IF EXISTS sce_tag_iov_map;

CREATE TABLE global_tag_map (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  global_tag TEXT UNIQUE NOT NULL,
  sce_tag TEXT NOT NULL
);

CREATE TABLE sce_tag_iov_map (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tag TEXT NOT NULL,
  run_number INTEGER NOT NULL,
  hash TEXT NOT NULL
);