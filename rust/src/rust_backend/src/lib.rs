use std::cell::Cell;

thread_local! {
    static START_TIME: Cell<u64> = Cell::new(ic_cdk::api::time());
    static START_BALANCE: Cell<u64> = Cell::new(ic_cdk::api::canister_balance());
    static COUNT: Cell<u64> = Cell::new(0);
}

#[export_name = "canister_heartbeat"]
fn heartbeat() {
    COUNT.with(|x| x.replace(x.get() + 1));
}

#[ic_cdk_macros::update]
fn reset() {
    START_TIME.with(|x| x.replace(ic_cdk::api::time()));
    START_BALANCE.with(|x| x.replace(ic_cdk::api::canister_balance()));
    COUNT.with(|x| x.replace(0));
}

#[ic_cdk_macros::update]
fn report() -> String {
    let time = (ic_cdk::api::time() - START_TIME.with(|x| x.get())) / 1_000_000;
    let count = COUNT.with(|x| x.get());
    let heartbeat_rate = time / count;
    let balance = ic_cdk::api::canister_balance();
    let burned = START_BALANCE.with(|x| x.get()) - balance;
    let burn_rate = 1_000 * burned / time;
    let burn_rate_bc_year = (60 * 60 * 24 * 365 * burn_rate) / 1_000_000_000;

    String::from(format!(
        "
        time, ms             : {time}
        heartbeat count      : {count}
        heartbeat rate, ms   : {heartbeat_rate}
        balance, Cycles      : {balance}
        burned, Cycles       : {burned}
        burn rate, Cycles/s  : {burn_rate}
        burn rate, BCycles/y : {burn_rate_bc_year}
    "
    ))
}
