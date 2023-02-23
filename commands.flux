_sum_turns = from(bucket: "power_consumption_raw")
    |> range(start: -1h)
    |> filter(fn: (r) => r["_field"] == "turns")
    |> aggregateWindow(every: inf, fn: sum, createEmpty: false)
    |> yield(name: "Turns")

_mean_power_per_turn = from(bucket: "power_consumption_raw")
    |> range(start: -1h)
    |> filter(fn: (r) => r["_field"] == "power_per_turn")
    |> aggregateWindow(every: inf, fn: mean, createEmpty: false)
    |> yield(name: "Power_Per_Turn")

union(tables: [_sum_turns, _mean_power_per_turn])
    |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
    |> set(key: "_field", value: "current_power_consumption")
    |> map(fn: (r) => ({ r with _value: 1.0 / float(v: r.power_per_turn) * float(v: r.turns)}))

//------------------------------------------------------------------------------------------------------------------------------------------------------

import "math"

from(bucket: "power_consumption_raw")
    |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
    |> filter(fn: (r) => r["_measurement"] == "electricity_meter")
    |> top(n: 2, columns: ["_time"])
    |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
    |> elapsed(unit: 1s)
    |> map(fn: (r) => ({ r with elapsed: int(v: math.abs(x: float(v: r.elapsed))) }))
    |> set(key: "_field", value: "current_power_consumption")
    |> map(fn: (r) => ({ r with _value: 1.0 / float(v: r.power_per_turn) * float(v: r.turns) / float(v: r.elapsed) / 3600.0 * 1000.0 }))
    |> yield(name: "Elapsed")

//------------------------------------------------------------------------------------------------------------------------------------------------------

import "influxdata/influxdb/sample"

sample.data(set: "birdMigration")
    |> range(start: -5y, stop: -4y)
    |> filter(fn: (r) => r._measurement == "migration")
    |> aggregateWindow(every: 1mo, fn: mean)

//------------------------------------------------------------------------------------------------------------------------------------------------------

from(bucket: "power_consumption_raw")
  |> range(start: -1h)
  |> filter(fn: (r) => r["_field"] == "turns")
  |> aggregateWindow(every: inf, fn: sum, createEmpty: false)
  |> yield(name: "raw_sum")

  from(bucket: "power_consumption_aggregated_per_minute")
  |> range(start: -1h)
  |> filter(fn: (r) => r["_field"] == "turns")
  |> aggregateWindow(every: inf, fn: sum, createEmpty: false)
  |> yield(name: "per_minute_sum")

//------------------------------------------------------------------------------------------------------------------------------------------------------

import "date"
today = date.truncate(t: now(), unit: 1d)

from(bucket: "power_consumption_raw")
    |> range(start: -1y)
    |> filter(fn: (r) => r["_field"] == "turns")
    |> truncateTimeColumn(unit: 1m)

//------------------------------------------------------------------------------------------------------------------------------------------------------

import "testing"
import "array"
import "date"

got =
    array.from(
        rows: [
            {table: 1, _field: "t", _value: now()},
            {table: 1, _field: "t", _value: now()},
            {table: 1, _field: "t", _value: now()},
        ],
    )

testing.load(tables: got)

//------------------------------------------------------------------------------------------------------------------------------------------------------

import "dict"
import "sampledata"

positions =
    [
        "Manager": "Jane Doe",
        "Asst. Manager": "Jack Smith",
        "Clerk": "John Doe",
    ]

sampledata.string()
    |> map(fn: (r) => ({_time: r._time, exampleDict: display(v: positions)}))

//------------------------------------------------------------------------------------------------------------------------------------------------------

from(bucket: "power_consumption_aggregated_hourly")
  |> range(start: -1d)
  |> filter(fn: (r) => r["_field"] == "turns")
  |> aggregateWindow(every: 1d, fn: sum, createEmpty: false)
  |> set(key: "_field", value: "turns_mean")
  |> to(bucket: "power_consumption_aggregated_daily")

//------------------------------------------------------------------------------------------------------------------------------------------------------

from(bucket: "power_consumption_raw")
  |> range(start: -1m)
  |> filter(fn: (r) => r["_field"] == "power_per_turn")
  |> aggregateWindow(every: 1m, fn: max, createEmpty: false)
  |> to(bucket: "power_consumption_aggregated_per_minute")

//------------------------------------------------------------------------------------------------------------------------------------------------------

import "date"
today = date.truncate(t: now(), unit: 1m)
start = date.sub(d: 1m, from: today)

from(bucket: "power_consumption_raw")
    |> range(start: start, stop: today)
    |> filter(fn: (r) => r["_field"] == "turns")
    |> truncateTimeColumn(unit: 1m)
    |> aggregateWindow(every: 1m, fn: sum, createEmpty: false)
    |> truncateTimeColumn(unit: 1m)
    |> yield(name: "today")

from(bucket: "power_consumption_raw")
    |> range(start: -2m)
    |> filter(fn: (r) => r["_field"] == "turns")
    |> truncateTimeColumn(unit: 1m)
    |> aggregateWindow(every: 1m, fn: sum, createEmpty: false)
    |> yield(name: "strat")