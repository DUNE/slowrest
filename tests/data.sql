INSERT INTO global_tag_map (global_tag, sce, lifetime)
VALUES
  ('1.0', '1.0', '1.0'),
  ('2.0', '4.0', '2.0');

INSERT INTO sce (tag, run_number, hash)
VALUES
  ('1.0', '5843', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root'),
  ('1.0', '5844', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root'),
  ('1.0', '5845', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root'),
  ('4.0', '5843', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root'),
  ('4.0', '5844', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root'),
  ('4.0', '5845', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root');

INSERT INTO lifetime (tag, run_number, hash)
VALUES
  ('1.0', '5843', 'dasflksad'),
  ('1.0', '5844', 'asdopsiau'),
  ('1.0', '5845', 'uiyadanko'),
  ('2.0', '5843', 'opiuasdnn'),
  ('2.0', '5844', 'posadiubb'),
  ('2.0', '5845', 'qweaasdmn');

INSERT INTO payload (hash, payload)
VALUES
  ('dasflksad', hex('1.542007e+09  94.606321  33.542739  4.918960e+02')),
  ('asdopsiau', hex('1.541765e+09  64.694125  28.832259  144.351408')),
  ('uiyadanko', hex('1.541492e+09  27.765317  18.096682  36.391442')),
  ('opiuasdnn', hex('1.541533e+09  27.236190  17.867753  35.492452')),
  ('posadiubb', hex('1.541533e+09  30.729682  19.307733  41.664970')),
  ('qweaasdmn', hex('1.541587e+09  39.686640  22.506454  60.009939'));


---------------------------------- EXPERIMENTAL ----------------------------------
INSERT INTO global_tag_map_new (global_tag, kind, tag)
VALUES
  ('1.0', 'sce', '1.0'),
  ('1.0', 'lifetime', '1.0'),
  ('2.0', 'sce', '4.0'),
  ('2.0', 'lifetime', '2.0');

INSERT INTO hash_map (kind, tag, run_number, hash)
VALUES
  ('sce', '1.0', '5843', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root'),
  ('sce', '1.0', '5844', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root'),
  ('sce', '1.0', '5845', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV.root'),
  ('sce', '4.0', '5843', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root'),
  ('sce', '4.0', '5844', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root'),
  ('sce', '4.0', '5845', '/cvmfs/dune.opensciencegrid.org/products/dune/dune_pardata/v01_80_00/SpaceChargeProtoDUNE/SCE_DataDriven_180kV_v4.root'),
  ('lifetime', '1.0', '5843', 'dasflksad'),
  ('lifetime', '1.0', '5844', 'asdopsiau'),
  ('lifetime', '1.0', '5845', 'uiyadanko'),
  ('lifetime', '2.0', '5843', 'opiuasdnn'),
  ('lifetime', '2.0', '5844', 'posadiubb'),
  ('lifetime', '2.0', '5845', 'qweaasdmn');
