use std::time::{Duration, Instant};

#[derive(Debug, Clone)]
struct TimeoutException {
    timer: TestTimer,
}

impl TimeoutException {
    fn new(timeout_seconds: u64) -> Self {
        TimeoutException {
            timer: TestTimer::new(timeout_seconds),
        }
    }

    fn get_timer(&self) -> TestTimer {
        self.timer.clone()
    }
}

#[derive(Debug, Clone)]
pub struct TestTimer {
    start_time: Instant,
    timeout_duration: Duration,
}

impl TestTimer {
    fn new(timeout_seconds: u64) -> Self {
        TestTimer {
            start_time: Instant::now(),
            timeout_duration: Duration::from_secs(timeout_seconds),
        }
    }

    fn elapsed(&self) -> Duration {
        self.start_time.elapsed()
    }

    fn is_timeout(&self) -> bool {
        self.elapsed() >= self.timeout_duration
    }
}
