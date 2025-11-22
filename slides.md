---
marp: true
theme: default
paginate: true
header: 'API Gateway Documentation v2.0'
footer: '23f2000060@ds.study.iitm.ac.in'
style: |
  section {
    background-color: #ffffff;
    font-family: 'Arial', sans-serif;
    color: #1a1a1a;
  }
  h1 {
    color: #0066cc;
    border-bottom: 3px solid #0066cc;
    padding-bottom: 10px;
  }
  h2 {
    color: #0052a3;
  }
  code {
    background-color: #f5f5f5;
    padding: 2px 6px;
    border-radius: 3px;
  }
  pre {
    background-color: #2d2d2d;
    padding: 15px;
    border-radius: 5px;
  }
  table {
    margin: 20px auto;
  }
  th {
    background-color: #0066cc;
    color: white;
  }
---

<!-- Title Slide -->
# API Gateway Documentation
## Enterprise-Grade API Management Platform

**Version 2.0 | 2024**

Contact: 23f2000060@ds.study.iitm.ac.in

---

# Table of Contents

1. Introduction & Architecture
2. Getting Started
3. Core Features
4. Mathematical Foundations
5. Performance Metrics
6. Security Features
7. Best Practices

---

# Introduction

## What is API Gateway?

API Gateway is a high-performance, scalable API management solution designed for modern microservices architectures.

**Key Benefits:**
- High Throughput: Handle millions of requests per second
- Low Latency: Sub-millisecond response times
- Flexible Routing: Dynamic path-based routing
- Built-in Security: OAuth2, JWT, API Keys

---

# Architecture Overview

## Core Components

**Gateway Core**: Request processing engine with $O(1)$ routing complexity

**Rate Limiter**: Token bucket algorithm implementation

**Load Balancer**: Multiple strategies (round-robin, least-connection)

**Cache Layer**: Redis-backed response cache with $O(1)$ lookup

---

# Mathematical Foundations

## Queueing Theory

**M/M/1 Queue Response Time:**

$$
W = \frac{1}{\mu - \lambda}
$$

where $\mu$ = service rate, $\lambda$ = arrival rate (requires $\lambda < \mu$)

**System Utilization:**

$$
\rho = \frac{\lambda}{\mu}, \quad 0 \leq \rho < 1
$$

---

# Rate Limiting Algorithm

## Token Bucket Implementation

$$
\text{tokens}(t) = \min\left(b, \text{tokens}(t-1) + r \times \Delta t\right)
$$

Where:
- $b$ = bucket capacity
- $r$ = refill rate (tokens per second)
- $\Delta t$ = time elapsed since last update

**Request Acceptance Condition:**

$$
\text{accept} = \begin{cases} 
\text{true} & \text{if tokens}(t) \geq 1 \\
\text{false} & \text{otherwise}
\end{cases}
$$

---

# Performance Calculations

## Throughput Formula

$$
T_{\max} = \frac{C \times N}{L_{\text{avg}} + P_{\text{avg}}}
$$

- $C$ = connections per server
- $N$ = number of servers
- $L_{\text{avg}}$ = average network latency
- $P_{\text{avg}}$ = average processing time

## Little's Law

$$
L = \lambda \times W
$$

$L$ = average requests in system, $\lambda$ = arrival rate, $W$ = average time

---

# Installation Guide

## Quick Start

```bash
# Install via npm
npm install @company/api-gateway

# Using Docker
docker pull company/api-gateway:latest
docker run -p 8080:8080 company/api-gateway:latest
```

## Basic Configuration

```yaml
gateway:
  port: 8080
  routes:
    - path: /api/v1/*
      backend: https://backend.example.com
      methods: [GET, POST, PUT, DELETE]
```

---

# Load Balancing Strategies

## Algorithm Complexity

| Strategy | Time Complexity | Best For |
|----------|----------------|----------|
| Round Robin | $O(1)$ | Even distribution |
| Least Connection | $O(\log n)$ | Variable load |
| IP Hash | $O(1)$ | Session affinity |

**Consistent Hashing Load Distribution:**

$$
\sigma = \sqrt{\frac{1}{m} \sum_{i=1}^{m} \left(\frac{n_i}{n} - \frac{1}{m}\right)^2}
$$

where $\sigma$ = standard deviation of load distribution

---

# Performance Benchmarks

| Metric | Value | Target |
|--------|-------|--------|
| Throughput | 50,000 req/s | 40,000 req/s |
| P50 Latency | 2 ms | < 5 ms |
| P99 Latency | 15 ms | < 20 ms |
| CPU Usage | 45% | < 60% |
| Memory Usage | 2.1 GB | < 3 GB |
| Uptime | 99.99% | 99.9% |

**Testing Environment:** AWS c5.2xlarge (8 vCPU, 16GB RAM)

---

# Cache Optimization

## Cache Hit Rate Calculation

$$
\text{Hit Rate} = \frac{N_{\text{hits}}}{N_{\text{hits}} + N_{\text{misses}}} \times 100\%
$$

## Expected Response Time

$$
E[T] = p \cdot T_{\text{cache}} + (1-p) \cdot T_{\text{backend}}
$$

where $p$ is the cache hit probability

**Typical Values:**
- $T_{\text{cache}}$ = 1-2 ms
- $T_{\text{backend}}$ = 50-200 ms
- Target $p$ > 0.8 (80% hit rate)

---

<!-- _backgroundImage: url(https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80) -->
<!-- _color: white -->

<div style="background-color: rgba(0, 0, 0, 0.75); padding: 40px; border-radius: 10px;">

# Global Infrastructure

## Deployed Across 12 Regions Worldwide

- **North America:** 4 availability zones
- **Europe:** 4 availability zones  
- **Asia Pacific:** 3 availability zones
- **South America:** 1 availability zone

### 99.99% Uptime SLA

**Edge Locations:** 50+ cities globally

</div>

---

# Security Features

## Authentication Methods

1. **API Keys** - Simple token-based authentication
2. **OAuth 2.0** - Industry standard authorization
3. **JWT Tokens** - Stateless authentication
4. **mTLS** - Certificate-based mutual authentication

## Security Headers

```javascript
headers: {
  'X-Frame-Options': 'DENY',
  'X-Content-Type-Options': 'nosniff',
  'Strict-Transport-Security': 'max-age=31536000',
  'Content-Security-Policy': "default-src 'self'"
}
```

---

# Connection Pooling

## Optimization Formula

**Optimal Pool Size:**

$$
n = \left\lceil \frac{R_{\max}}{C_b} \right\rceil
$$

where:
- $R_{\max}$ = maximum concurrent requests
- $C_b$ = connections per backend server

**Typical Configuration:**
- $R_{\max}$ = 1000 requests
- $C_b$ = 50 connections
- Optimal $n$ = 20 pools

---

# Request Batching

## Efficiency Gains

**Amortized Time Complexity:**

Individual requests: $O(n)$ for $n$ requests

Batched requests: $O(1)$ amortized

**Latency Reduction:**

$$
L_{\text{batched}} = \frac{L_{\text{single}}}{b} + \Delta t_{\text{batch}}
$$

where $b$ = batch size, $\Delta t_{\text{batch}}$ = batching overhead

---

# Compression

## Compression Ratio

$$
r = \frac{S_{\text{original}}}{S_{\text{compressed}}}
$$

**Transfer Time Saved:**

$$
\Delta T = \frac{S_{\text{original}} - S_{\text{compressed}}}{B}
$$

where $B$ = bandwidth

| Format | Compression Ratio | Use Case |
|--------|------------------|----------|
| gzip | 3-10x | JSON/Text |
| Brotli | 5-15x | Static assets |
| zstd | 4-12x | Real-time streaming |

---

# Monitoring & Observability

## Key Metrics to Track

**Golden Signals:**
1. Latency - Response time distribution
2. Traffic - Request rate (requests/second)
3. Errors - Error rate percentage
4. Saturation - Resource utilization

**Prometheus Query Example:**

```promql
# 99th percentile latency
histogram_quantile(0.99, 
  rate(http_request_duration_seconds_bucket[5m])
)
```

---

# Circuit Breaker Pattern

## State Transitions

```
CLOSED → OPEN → HALF_OPEN → CLOSED
```

**Failure Rate Threshold:**

$$
f = \frac{N_{\text{failures}}}{N_{\text{total}}} > \theta
$$

If $f > \theta$ (e.g., 0.5), transition to OPEN state

**Recovery:** After timeout period, transition to HALF_OPEN for testing

---

# Capacity Planning

## Percentile Calculation

For sorted response times $[t_1, t_2, \ldots, t_n]$:

$$
P_{xx} = t_{\left\lceil \frac{xx \cdot n}{100} \right\rceil}
$$

## Tail Latency Amplification

When calling $k$ microservices in parallel:

$$
P_{99}^{\text{composite}} = 1 - (1 - P_{99}^{\text{single}})^k
$$

**Example:** With $k=10$ services, $P_{99}=0.01$:
$P_{99}^{\text{composite}} \approx 0.096$ (9.6% slower requests)

---

# Consistent Hashing

## Jump Consistent Hash

$$
h(k, b) = \arg\max_{j \in [0,b)} \left\{ j : \text{random}(k, j) < \frac{j}{b} \right\}
$$

**Properties:**
- Time: $O(\log n)$ average case
- Space: $O(1)$ - no lookup table needed
- Minimal key redistribution on server changes

**Bounded Load Formula:**

$$
\text{load}(s) \leq \left\lceil \frac{1 + \epsilon}{n} \cdot L_{\text{total}} \right\rceil
$$

---

# Best Practices

## 1. Rate Limiting Strategy

- Use sliding window for accuracy
- Implement distributed rate limiting with Redis
- Set per-user and global limits

## 2. Caching Policy

- Cache GET requests only
- Use ETags for cache validation
- Implement cache warming for critical paths

## 3. Error Handling

- Return meaningful error codes (4xx, 5xx)
- Include request IDs for tracing
- Implement graceful degradation

---

# Deployment Strategies

## Blue-Green Deployment

1. Deploy new version to "green" environment
2. Run smoke tests and validation
3. Switch traffic from "blue" to "green"
4. Keep "blue" for rollback (< 30 seconds)

## Canary Release

Progressive rollout: 5% → 25% → 50% → 100%

**Error Rate Monitoring:**

$$
e_{\text{canary}} = \frac{N_{\text{errors}}}{N_{\text{requests}}} \times 100\%
$$

Auto-rollback if $e_{\text{canary}} > e_{\text{baseline}} \times 1.5$

---

# Advanced Features Roadmap

## Q1 2025 Planned Features

- GraphQL Support - Native GraphQL gateway
- gRPC Protocol - HTTP/2 and gRPC proxying
- AI-Powered Analytics - ML-based anomaly detection
- Multi-Cloud Mesh - Seamless cloud provider integration
- WebSocket Support - Real-time bidirectional communication

**Performance Target:** Maintain $P_{99} < 20ms$ at 100K req/s

---

# Troubleshooting Guide

| Issue | Cause | Solution |
|-------|-------|----------|
| High latency | Backend slow | Enable caching |
| 503 errors | Rate limiting | Increase limits |
| Memory leak | Cache overflow | Set maxSize |
| Timeout errors | Network issues | Tune timeouts |

**Debug Mode:**

```bash
LOG_LEVEL=debug npm start
# Provides detailed request/response logging
```

---

# Configuration Example

## Complete Gateway Setup

```typescript
interface GatewayConfig {
  port: number;
  host: string;
  cors: {
    enabled: boolean;
    origins: string[];
  };
  rateLimit: {
    windowMs: number;
    max: number;
  };
  routes: Route[];
}
```

**Documentation:** https://docs.company.com/api-gateway

---

# Summary

## Key Takeaways

- **Performance:** $O(1)$ routing, sub-millisecond latency
- **Scalability:** Horizontal scaling with consistent hashing
- **Reliability:** Circuit breakers, health checks, auto-retry
- **Security:** Multiple auth methods, encryption at rest/transit
- **Observability:** Metrics, tracing, logging integration

**Mathematical Optimization:** Queueing theory ensures optimal resource utilization

---

# Thank You

## Questions?

**Documentation:** https://docs.company.com
**Support:** support@company.com
**Email:** 23f2000060@ds.study.iitm.ac.in

**GitHub Repository:**
```
https://github.com/company/api-gateway
```

**Join our Slack:** #api-gateway-support

---

# References

1. **RFC 7231** - HTTP/1.1 Semantics and Content
2. **RFC 6749** - OAuth 2.0 Authorization Framework
3. **RFC 7519** - JSON Web Token (JWT)
4. **Karger et al.** - Consistent Hashing and Random Trees
5. **Fowler, M.** - Patterns of Enterprise Application Architecture
6. **Little, J.D.C.** - A Proof for the Queuing Formula: L = λW

**Version Control:**
This presentation is maintained in version control and can be accessed via GitHub raw URL.
