INSERT INTO global_tag_map (global_tag, sce, lifetime)
VALUES
  ('1.0', '1.0', '1.0'),
  ('2.0', '4.0', '2.0');

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
  ('dasflksad', hex('1.542007e+09   94.606321  33.542739  4.918960e+02')),
  ('asdopsiau', 1),
  ('uiyadanko', 2),
  ('opiuasdnn', 0),
  ('posadiubb', 1),
  ('qweaasdmn', 2);
