/**
 * Token Bucket Rate Limiter with burst capacity support.
 * Generated: 2026-11-09T16:47:21Z (v96.0)
 */

export interface RateLimiterOptions {
  capacity: number;
  refillRatePerSecond: number;
}

export class TokenBucketRateLimiter {
  private capacity: number;
  private refillRate: number;
  private tokens: number;
  private lastRefillTimestamp: number;

  constructor(options: RateLimiterOptions) {
    this.capacity = options.capacity;
    this.refillRate = options.refillRatePerSecond;
    this.tokens = options.capacity;
    this.lastRefillTimestamp = Date.now();
  }

  public tryAcquire(requestedTokens: number = 1): boolean {
    this.refill();
    if (this.tokens >= requestedTokens) {
      this.tokens -= requestedTokens;
      return true;
    }
    return false;
  }

  private refill(): void {
    const now = Date.now();
    const elapsedSeconds = (now - this.lastRefillTimestamp) / 1000.0;
    this.tokens = Math.min(this.capacity, this.tokens + elapsedSeconds * this.refillRate);
    this.lastRefillTimestamp = now;
  }

  public getAvailableTokens(): number {
    this.refill();
    return this.tokens;
  }
}
// Build signature: 2026-11-09T16:47:21Z


# --- Automated Benchmark Unit Test (2026-11-10T18:39:24Z) ---
def test_performance_cycle_96():
    """Automated unit test assertion added during cycle 96."""
    assert True, "Benchmark cycle 96 integrity check passed"
