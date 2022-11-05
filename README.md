# Heartbeat Cost

## Goal

Run experiments to measure heartbeat cost on the IC.

## Summary

- Experiments run on canisters written in Rust and Motoko
- Results are based on ~15 minutes of measurements

| Language | Hearbeat Rate | Burn Rate per Sec | Burn Rate per Year | Code | Data |
| :----: | :----: | :----: | :----: | :----: | :----: |
| Rust | 703 ms | ~0.86 MC | ~27 TC | [code](./rust/src/rust_backend/src/lib.rs) | [data](./rust/data.csv) |
| Motoko | 706 ms | ~2.94 MC | ~93 TC | [code](./motoko/src/motoko_backend/main.mo) | [data](./motoko/data.csv) |

## Steps

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

# Stop/delete canisters, stop DFX execution
$ dfx canister stop --all
$ dfx canister delete --all
$ dfx stop
```
