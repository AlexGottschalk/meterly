import "date"
import "math"

today = date.truncate(t: now(), unit: 1d)

sumTurns = from(bucket: "power_consumption_raw")
    |> range(start: today)
    |> filter(fn: (r) => r["_measurement"] == "electricity_meter")
    |> filter(fn: (r) => r["location"] == "home")
    |> filter(fn: (r) => r["_field"] == "turns")
    |> aggregateWindow(every: inf, fn: sum, createEmpty: false)

meanPowerPerTurn = from(bucket: "power_consumption_raw")
    |> range(start: today)
    |> filter(fn: (r) => r["_measurement"] == "electricity_meter")
    |> filter(fn: (r) => r["location"] == "home")
    |> filter(fn: (r) => r["_field"] == "power_per_turn")
    |> aggregateWindow(every: inf, fn: mean, createEmpty: false)

union(tables: [sumTurns, meanPowerPerTurn])
    |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
    |> set(key: "_field", value: "total_power_consumption_today")
    |> map(fn: (r) => ({ _value: float(v: r.turns) / float(v: r.power_per_turn)}))