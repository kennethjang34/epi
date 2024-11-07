use std::time::{Duration, Instant};

struct TestTimer {
    second_to_micro: u64,
    start: Instant,
    duration_us: u128,
}

impl TestTimer {
    const SECOND_TO_MICRO: u128 = 1_000_000;

    fn new(duration_seconds: Option<u128>) -> Self {
        let duration_us = match duration_seconds {
            Some(seconds) => seconds * TestTimer::SECOND_TO_MICRO,
            None => 0,
        };

        TestTimer {
            second_to_micro: 1_000_000,
            start: Instant::now(),
            duration_us,
        }
    }

    fn start(&mut self) {
        self.start = Instant::now();
    }

    fn stop(&mut self) {
        self.duration_us += self.start.elapsed().as_micros();
    }

    fn get_microseconds(&self) -> u128 {
        self.duration_us
    }
}

fn duration_to_string(dur: u64) -> String {
    let dur = dur as i64;
    let milli_to_micro = 1000;
    let second_to_micro = milli_to_micro * 1000;

    if dur == 0 {
        return "  <1 us".to_string();
    } else if dur < milli_to_micro {
        return format!("{:>4} us", dur);
    } else if dur < second_to_micro {
        return format!("{:>4} ms", dur / milli_to_micro);
    }
    return format!("{:>4}  s", dur / second_to_micro);
}

fn avg_and_median_from_durations(durations: &Vec<u64>) -> (f64, f64) {
    let mean = durations.iter().sum::<u64>() as f64 / durations.len() as f64;
    let median = {
        let mut sorted_durations = durations.clone();
        sorted_durations.sort();

        if sorted_durations.len() % 2 == 0 {
            let mid = sorted_durations.len() / 2;
            (sorted_durations[mid - 1] as f64 + sorted_durations[mid] as f64) / 2.0
        } else {
            sorted_durations[sorted_durations.len() / 2] as f64
        }
    };

    (mean, median)
}
