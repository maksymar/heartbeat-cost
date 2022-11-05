import Cycles "mo:base/ExperimentalCycles";
import Int "mo:base/Int";
import Text "mo:base/Text";
import Time "mo:base/Time";

actor {
  var start_time = Time.now();
  var start_balance = Cycles.balance() : Int;
  var count = 0;

  system func heartbeat() : async () {
    count += 1;
  };

  public func reset() {
    start_time := Time.now();
    start_balance := Cycles.balance() : Int;
    count := 0;
  };

  public func report() : async Text {
    var time = (Time.now() - start_time) / 1_000_000;
    var heartbeat_rate = time / count;
    var balance = Cycles.balance() : Int;
    var burned = start_balance - balance;
    var burn_rate = 1_000 * burned / time;
    var burn_rate_bc_year = (60 * 60 * 24 * 365 * burn_rate) / 1_000_000_000;

    var t = "";
    t := Text.concat(t, "\n lang : motoko");
    t := Text.concat(t, Text.concat("\n time, ms             : ", Int.toText(time)));
    t := Text.concat(t, Text.concat("\n heartbeat count      : ", Int.toText(count)));
    t := Text.concat(t, Text.concat("\n heartbeat rate, ms   : ", Int.toText(heartbeat_rate)));
    t := Text.concat(t, Text.concat("\n balance, Cycles      : ", Int.toText(balance)));
    t := Text.concat(t, Text.concat("\n burned, Cycles       : ", Int.toText(burned)));
    t := Text.concat(t, Text.concat("\n burn rate, Cycles/s  : ", Int.toText(burn_rate)));
    t := Text.concat(t, Text.concat("\n burn rate, BCycles/y : ", Int.toText(burn_rate_bc_year)));
    t := Text.concat(t, "\n ");
    return t;
  };
};
