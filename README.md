# Heartbeat Cost

## Goal

Run experiments to measure heartbeat cost on the IC.

## Summary

- Experiments run on canisters written in Rust and Motoko
  - Empty canisters `*_empty`, time is measured outside of `dfx` call
  - Non-empty canisters with measurements done inside the canister
- Results are based on ~15 minutes of measurements

| Experiment | Hearbeat Rate | Burn Rate per Sec | Burn Rate per Year | Code | Data |
| :----: | :----: | :----: | :----: | :----: | :----: |
| `rust` | 703 ms | ~0.86 MC | ~27 TC | [code](./rust/src/rust_backend/src/lib.rs) | [data](./rust/data.csv) |
| `rust_empty` | - | ~0.86 MC | ~27 TC | [code](./rust_empty/src/rust_backend/src/lib.rs) | [data](./rust_empty/data.csv) |
| `motoko` | 706 ms | ~2.94 MC | ~93 TC | [code](./motoko/src/motoko_backend/main.mo) | [data](./motoko/data.csv) |
| `motoko_empty` | - | ~3.01 MC | ~95 TC | [code](./motoko_empty/src/motoko_backend/main.mo) | [data](./motoko_empty/data.csv) |

## Experiments `rust`, `motoko`

```bash
# Enter either motoko or rust folder.
$ cd motoko
# or
$ cd rust

# Start DFX and deploy a canister.
$ dfx start --background
$ dfx deploy

# Open Candid UI
# - call "reset" function to start measurements
# - call "report" function to get statistics since the last reset

# Stop/delete canisters, stop DFX execution.
$ dfx canister stop --all
$ dfx canister delete --all
$ dfx stop
```

## Experiments `rust_empty`, `motoko_empty`

```bash
# Enter either motoko_empty or rust_empty folder.
$ cd motoko_empty
# or
$ cd rust_empty

# Start DFX and deploy a canister.
$ dfx start --background
$ dfx deploy

# Run experiment.
$ ./run_experiment.py

# Stop/delete canisters, stop DFX execution.
$ dfx canister stop --all
$ dfx canister delete --all
$ dfx stop
```
